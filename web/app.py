from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
from datetime import date, datetime, timedelta
import random
import hashlib

app = Flask(__name__)
app.secret_key = "starbucks_secret_key_nhom11"

# ================= 1. KẾT NỐI DATABASE =================
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# Hàm băm mật khẩu bảo mật (SHA-256)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ================= 2. HỆ THỐNG ĐĂNG NHẬP & AUTH =================
@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]
        p_hashed = hash_password(p)

        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (u, p_hashed)
        ).fetchone()
        db.close()

        if user:
            session["user"] = user["username"]
            session["role"] = user["role"]
            if user["role"] == "admin":
                return redirect(url_for("dashboard_admin"))
            else:
                return redirect(url_for("dashboard_staff"))
        else:
            error = "Sai tài khoản hoặc mật khẩu!"

    return render_template("login.html", error=error)

@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        db = get_db()
        user = db.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
        db.close()
        if not user:
            error = "Tài khoản không tồn tại!"
        else:
            otp = str(random.randint(100000, 999999))
            session["otp"] = otp
            session["otp_user"] = username
            session["otp_expire"] = (datetime.now() + timedelta(minutes=5)).isoformat()
            print(f"--- MÃ OTP CHO {username} LÀ: {otp} ---") # Xem ở console
            return redirect(url_for("verify_otp"))
    return render_template("forgot_password.html", error=error)

@app.route("/verify-otp", methods=["GET", "POST"])
def verify_otp():
    error = None
    if request.method == "POST":
        if request.form["otp"] == session.get("otp"):
            if datetime.now() <= datetime.fromisoformat(session["otp_expire"]):
                session["verified"] = True
                return redirect(url_for("reset_password"))
            else:
                error = "OTP đã hết hạn!"
        else:
            error = "Mã OTP không đúng!"
    return render_template("verify_otp.html", error=error)

@app.route("/reset-password", methods=["GET", "POST"])
def reset_password():
    if not session.get("verified"): return redirect(url_for("login"))
    if request.method == "POST":
        new_p = hash_password(request.form["new_password"])
        db = get_db()
        db.execute("UPDATE users SET password=? WHERE username=?", (new_p, session["otp_user"]))
        db.commit()
        db.close()
        session.clear()
        return redirect(url_for("login"))
    return render_template("reset_password.html")

# ================= 3. DASHBOARD (ADMIN & STAFF) =================
@app.route("/dashboard/admin")
def dashboard_admin():
    if session.get("role") != "admin": return redirect(url_for("login"))
    db = get_db()
    tables = db.execute("SELECT * FROM tables").fetchall()
    rev_d = db.execute("SELECT SUM(total) FROM invoices WHERE DATE(created_at)=DATE('now') AND status='paid'").fetchone()[0] or 0
    rev_m = db.execute("SELECT SUM(total) FROM invoices WHERE strftime('%Y-%m', created_at)=strftime('%Y-%m','now') AND status='paid'").fetchone()[0] or 0
    db.close()
    return render_template("dashboard_admin.html", tables=tables, revenue_day=rev_d, revenue_month=rev_m)

@app.route("/dashboard/staff")
def dashboard_staff():
    if session.get("role") != "staff": return redirect(url_for("login"))
    db = get_db()
    tables = db.execute("SELECT * FROM tables").fetchall()
    db.close()
    return render_template("dashboard_staff.html", tables=tables)

# ================= 4. QUẢN LÝ BÀN (TB04/05) =================
@app.route("/tables")
def tables_list():
    if "user" not in session: return redirect(url_for("login"))
    db = get_db()
    tables = db.execute("SELECT * FROM tables").fetchall()
    db.close()
    return render_template("tables_list.html", tables=tables)

@app.route("/tables/update", methods=["POST"])
def table_update():
    if "user" not in session: return jsonify(success=False), 403
    data = request.json
    db = get_db()
    db.execute("UPDATE tables SET status=? WHERE id=?", (data.get("status"), data.get("id")))
    db.commit()
    db.close()
    return jsonify(success=True)

# ================= 5. BÁO CÁO DOANH THU (DT01/02/03) =================

@app.route("/revenue/day")
def revenue_day():
    if session.get("role") != "admin": return redirect(url_for("login"))
    selected_date = request.args.get("date") or date.today().isoformat()
    db = get_db()
    invoices = db.execute("SELECT * FROM invoices WHERE DATE(created_at)=? AND status='paid' ORDER BY created_at DESC", (selected_date,)).fetchall()
    total = sum(inv["total"] for inv in invoices)
    db.close()
    return render_template("revenue_day.html", invoices=invoices, total=total, selected_date=selected_date)

@app.route("/revenue/month")
def revenue_month():
    if session.get("role") != "admin": return redirect(url_for("login"))
    month = request.args.get("month") or date.today().strftime("%Y-%m")
    db = get_db()
    chart_data = db.execute("""
        SELECT DATE(created_at) as day, SUM(total) as daily_total 
        FROM invoices WHERE strftime('%Y-%m', created_at)=? AND status='paid' 
        GROUP BY day ORDER BY day ASC
    """, (month,)).fetchall()
    total = sum(d["daily_total"] for d in chart_data)
    db.close()
    return render_template("revenue_month.html", chart_data=chart_data, total=total, month=month)

@app.route("/invoice/<int:invoice_id>")
def invoice_detail(invoice_id):
    if "user" not in session: return redirect(url_for("login"))
    db = get_db()
    invoice = db.execute("SELECT * FROM invoices WHERE id=?", (invoice_id,)).fetchone()
    items = db.execute("SELECT * FROM invoice_items WHERE invoice_id=?", (invoice_id,)).fetchall()
    db.close()
    if not invoice: return "Hóa đơn không tồn tại", 404
    return render_template("invoice_detail.html", invoice=invoice, items=items)

# ================= 6. ĐĂNG XUẤT =================
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)