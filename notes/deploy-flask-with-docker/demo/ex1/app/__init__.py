from os import environ
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    env_1 = environ.get('ENV_VARIABLE_FROM_DOCKER')
    return jsonify('Ex1, {}'.format(env_1)), 200

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return '{0} + {1} = {2}'.format(a, b, a+b)
