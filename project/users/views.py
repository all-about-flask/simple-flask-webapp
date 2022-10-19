from sqlite3 import IntegrityError

from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask_login import logout_user, login_required
from sqlalchemy.sql.functions import current_user

from project.ext import db
from flask_login import login_user
from project.models import User
from project.users.form import RegisterForm, LoginForm

users_blueprint = Blueprint('users', __name__)
# login_required =


# @users_blueprint.route('/login')
# def login():
#     return render_template('login.html')


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
                return redirect(url_for('recipes.index'))
            except IntegrityError:
                db.session.rollback()
                flash('ERROR! Email ({}) already exists.'.format(form.email.data), 'error')
                return render_template('register.html', form=form)
    return render_template('register.html', form=form)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST':
        if form.validate():
            user = User.query.filter_by(email=form.email.data).first()
            if user is not None and user.is_correct_password(form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user)
                # flash('Thanks for logging in, {}'.format(current_user))
                return redirect(url_for('recipes.index'))
            else:
                flash('ERROR! Incorrect login credentials.', 'error')
                return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@users_blueprint.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    # db.session.add(user)
    db.session.commit()
    logout_user()
    flash('Goodbye', 'info')
    return redirect(url_for('users.login'))
