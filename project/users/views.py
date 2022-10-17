from flask import render_template, Blueprint

from project import app


user_blueprint = Blueprint('users', __name__, template_folder='templates')

@user_blueprint.route('/login')
def login():
    return render_template('login.html')

