from flask import Flask
from .ext import db, migrate, login_manager

from project.users.views import users_blueprint
from project.recipes.views import recipes_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object('project.config.Baseconfig')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    app.register_blueprint(users_blueprint)
    app.register_blueprint(recipes_blueprint)
    return app
