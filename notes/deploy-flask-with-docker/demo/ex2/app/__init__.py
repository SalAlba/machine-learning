from os import environ

from flask import Flask, jsonify

from .modules.posts.views import current_blueprint

app = Flask(__name__)

app.register_blueprint(current_blueprint, url_prefix='/posts')


@app.route('/')
def hello_world():
    env_1 = environ.get('ENV_VARIABLE_FROM_DOCKER')
    return jsonify('Ex2, {}'.format(env_1)), 200

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return '{0} + {1} = {2}'.format(a, b, a+b)
