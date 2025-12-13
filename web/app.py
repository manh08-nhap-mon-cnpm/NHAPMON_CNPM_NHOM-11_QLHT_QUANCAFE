from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>QUẢN LÝ QUÁN CAFE</h1>
    <p>Web đầu tiên đã chạy 🎉</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
