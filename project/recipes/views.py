from flask import render_template, Blueprint, request, redirect, url_for, flash

from project.ext import db
from project.models import Recipe
from project.recipes.forms import AddRecipeForm

recipes_blueprint = Blueprint('recipes', __name__, template_folder='templates')


@recipes_blueprint.route('/')
def index():
    all_recipe = Recipe.query.all()
    return render_template('recipes.html', recipes=all_recipe)


@recipes_blueprint.route('/add', methods=['GET', 'POST'])
def add_recipe():
    form = AddRecipeForm(request.form)
    if request.method == 'POST':
        if form.validate():
            new_recipe = Recipe(form.recipe_title.data, form.recipe_description.data)
            flash('New recipe, {}, added!'.format(new_recipe.recipe_title), 'success')
            db.session.add(new_recipe)
            db.session.commit()
            return redirect(url_for('recipes.index'))
        else:
            flash('ERROR! Recipe was not added.', 'error')
    return render_template('add_recipe.html', form=form)
