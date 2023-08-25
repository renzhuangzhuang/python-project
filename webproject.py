from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<rzz>')
def user(rzz):
    return '<h1>Hello, %s!</h1>' % rzz
if __name__ == '__main__':
    app.run(debug=True)