from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return '{0} + {1} = {2}'.format(a, b, a+b)


if __name__ == "__main__":
    app.run()