from flask import Flask, render_template

# Khai báo cho Flask biết templates và static nằm trong folder 'web'
app = Flask(__name__, 
            template_folder='web/templates', 
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
    app.run(debug=True)