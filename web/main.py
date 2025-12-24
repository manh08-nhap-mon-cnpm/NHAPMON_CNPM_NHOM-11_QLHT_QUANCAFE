from flask import Flask, render_template

# Sửa dòng này: template_folder='.' nghĩa là tìm file HTML ngay tại thư mục gốc
app = Flask(__name__, 
            template_folder='.', 
            static_folder='web/static')

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
    app.run(debug=True, port=5000)