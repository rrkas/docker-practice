from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<H1>Hello, Docker!</H1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')