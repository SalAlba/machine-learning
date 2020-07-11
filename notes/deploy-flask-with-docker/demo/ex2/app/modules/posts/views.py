from flask import jsonify, render_template
# from flask_login import login_required

from ..posts import post_blueprint as current_blueprint

@current_blueprint.route('/', methods=['GET'])
# @login_required
def index():
    return render_template('index.html')