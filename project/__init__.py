from flask import Flask

from .ext import login_manager, db

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('project.config.Baseconfig')

from project.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()


from project.users.views import users_blueprint
from project.recipes.views import recipes_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(recipes_blueprint)
