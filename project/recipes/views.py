from flask import render_template, Blueprint

from project.models import Recipe

recipes_blueprint = Blueprint('recipes', __name__, template_folder='templates')


@recipes_blueprint.route('/')
def index():
    all_recipe = Recipe.query.all()
    return render_template('recipes.html', recipes=all_recipe)
