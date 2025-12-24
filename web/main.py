from flask import Flask, render_template
import os

# Sửa dòng này để Flask tìm file HTML ngay tại thư mục chứa file main.py
app = Flask(__name__, 
            template_folder='.', 
            static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/staff')
def staff():
    return render_template('staff.html')

if __name__ == '__main__':
    # Thêm cái này để chạy đúng port và dễ debug
    app.run(debug=True, port=5000)