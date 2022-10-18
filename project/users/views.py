from sqlite3 import IntegrityError

from flask import render_template, Blueprint, request, flash, redirect, url_for

from project.ext import db
from project.models import User
from project.users.form import RegisterForm

users_blueprint = Blueprint('users', __name__, template_folder='templates')


@users_blueprint.route('/login')
def login():
    return render_template('login.html')


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate():
            try:
                new_user = User(form.email.data, form.password.data)
                new_user.authenticated = True
                db.session.add(new_user)
                db.session.commit()
                flash('Thanks for registering!', 'success')
                return redirect(url_for('recipe.index'))
            except IntegrityError:
                db.session.rollback()
                flash('ERROR! Email({}) already exist.'.format(form.email.data), 'error')
                return render_template('register.html', form=form)
    return render_template('register.html', form=form)