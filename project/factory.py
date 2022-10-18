from flask import Flask
from .ext import db, migrate

from project.users.views import users_blueprint
from project.recipes.views import recipes_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object('project.config.Baseconfig')

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(users_blueprint)
    app.register_blueprint(recipes_blueprint)
    return app
