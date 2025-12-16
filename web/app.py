from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
from datetime import date

app = Flask(__name__)
app.secret_key = "starbucks_secret"

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# ===== LOGIN =====
@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]
        db = get_db()
        user = db.execute("SELECT * FROM users WHERE username=? AND password=?", (u,p)).fetchone()
        db.close()
        if not user:
            error = "Sai tài khoản hoặc mật khẩu"
        else:
            session["user"] = user["username"]
            session["role"] = user["role"]
            if user["role"] == "admin":
                return redirect(url_for("dashboard_admin"))
            return redirect(url_for("dashboard_staff"))
    return render_template("login.html", error=error)

# ===== DASHBOARD ADMIN =====
@app.route("/dashboard/admin")
def dashboard_admin():
    if session.get("role") != "admin":
        return redirect(url_for("login"))
    db = get_db()
    tables = db.execute("SELECT * FROM tables").fetchall()
    revenue_day = db.execute("SELECT SUM(total) AS total FROM invoices WHERE DATE(created_at)=?", (date.today().isoformat(),)).fetchone()["total"] or 0
    revenue_month = db.execute("SELECT SUM(total) AS total FROM invoices WHERE strftime('%Y-%m', created_at)=strftime('%Y-%m','now')").fetchone()["total"] or 0
    invoices = db.execute("SELECT * FROM invoices ORDER BY created_at DESC").fetchall()
    db.close()
    return render_template("dashboard_admin.html", tables=tables, revenue_day=revenue_day, revenue_month=revenue_month, invoices=invoices)

# ===== DASHBOARD STAFF =====
@app.route("/dashboard/staff")
def dashboard_staff():
    if session.get("role") != "staff":
        return redirect(url_for("login"))
    db = get_db()
    tables = db.execute("SELECT * FROM tables").fetchall()
    db.close()
    return render_template("dashboard_staff.html", tables=tables)

# ===== CHANGE PASSWORD =====
@app.route("/change-password", methods=["GET","POST"])
def change_password():
    if "user" not in session:
        return redirect(url_for("login"))
    error = None
    if request.method=="POST":
        old = request.form["old_password"]
        new = request.form["new_password"]
        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?", (session["user"], old))
        if not cur.fetchone():
            error = "Mật khẩu cũ không đúng"
        else:
            cur.execute("UPDATE users SET password=? WHERE username=?", (new, session["user"]))
            db.commit()
            session.clear()
            db.close()
            return redirect(url_for("login"))
        db.close()
    return render_template("change_password.html", error=error)

# ===== UPDATE TABLE STATUS =====
@app.route("/update-table", methods=["POST"])
def update_table():
    if "user" not in session:
        return jsonify(success=False), 403
    table_id = request.json["id"]
    status = request.json["status"]
    db = get_db()
    db.execute("UPDATE tables SET status=? WHERE id=?", (status, table_id))
    db.commit()
    db.close()
    return jsonify(success=True)

# ===== LOGOUT =====
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__=="__main__":
    app.run(debug=True)
# ===== DOANH THU =====
@app.route("/revenue/day")
def revenue_day():
    if "role" not in session or session["role"] != "admin":
        return redirect(url_for("login"))

    db = get_db()
    today = date.today().isoformat()
    total = db.execute(
        "SELECT SUM(total) as total FROM invoices WHERE DATE(created_at)=?",
        (today,)
    ).fetchone()["total"] or 0
    invoices = db.execute(
        "SELECT * FROM invoices WHERE DATE(created_at)=? ORDER BY created_at DESC",
        (today,)
    ).fetchall()
    db.close()
    return render_template("revenue_day.html", total=total, invoices=invoices, title="Doanh thu ngày")

@app.route("/revenue/month")
def revenue_month():
    if "role" not in session or session["role"] != "admin":
        return redirect(url_for("login"))

    db = get_db()
    month = date.today().strftime("%Y-%m")
    total = db.execute(
        "SELECT SUM(total) as total FROM invoices WHERE strftime('%Y-%m', created_at)=?",
        (month,)
    ).fetchone()["total"] or 0
    invoices = db.execute(
        "SELECT * FROM invoices WHERE strftime('%Y-%m', created_at)=? ORDER BY created_at DESC",
        (month,)
    ).fetchall()
    db.close()
    return render_template("revenue_month.html", total=total, invoices=invoices, title="Doanh thu tháng")

@app.route("/invoice/<int:invoice_id>")
def invoice_detail(invoice_id):
    if "role" not in session or session["role"] != "admin":
        return redirect(url_for("login"))

    db = get_db()
    invoice = db.execute("SELECT * FROM invoices WHERE id=?", (invoice_id,)).fetchone()
    db.close()
    if not invoice:
        return "Hóa đơn không tồn tại", 404
    return render_template("invoice_detail.html", invoice=invoice)
# ===== BÀN =====
@app.route("/tables")
def tables_list():
    if "role" not in session or session["role"] != "admin":
        return redirect(url_for("login"))

    db = get_db()
    tables = db.execute("SELECT * FROM tables").fetchall()
    db.close()
    return render_template("tables_list.html", tables=tables)

@app.route("/tables/update", methods=["POST"])
def table_update():
    if "role" not in session or session["role"] != "admin":
        return jsonify(success=False), 403

    table_id = request.json.get("id")
    status = request.json.get("status")
    db = get_db()
    db.execute("UPDATE tables SET status=? WHERE id=?", (status, table_id))
    db.commit()
    db.close()
    return jsonify(success=True)
