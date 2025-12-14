from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "katinat_secret_key"

USERS = {
    "admin": {"password": "123", "role": "admin"},
    "staff": {"password": "123", "role": "staff"}
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in USERS and USERS[username]["password"] == password:
            session["user"] = username
            session["role"] = USERS[username]["role"]

            if session["role"] == "admin":
                return redirect(url_for("dashboard_admin"))
            return redirect(url_for("dashboard_staff"))

    return render_template("login.html")

@app.route("/dashboard/admin")
def dashboard_admin():
    if "user" not in session or session["role"] != "admin":
        return redirect(url_for("login"))
    return render_template("dashboard_admin.html")

@app.route("/dashboard/staff")
def dashboard_staff():
    if "user" not in session or session["role"] != "staff":
        return redirect(url_for("login"))
    return render_template("dashboard_staff.html")

@app.route("/change-password", methods=["GET", "POST"])
def change_password():
    if request.method == "POST":
        return redirect(url_for("login"))
    return render_template("change_password.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
