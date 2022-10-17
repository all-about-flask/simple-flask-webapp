from flask import render_template, Blueprint

recipe_blueprint: Blueprint = Blueprint('recipes', __name__, template_folder='templates')


@recipe_blueprint.route('/')
def index():
    return render_template('index.html')
