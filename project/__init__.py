from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

db: SQLAlchemy = SQLAlchemy(app)

from project.users.views import user_blueprint
from project.recipes.views import recipe_blueprint

app.register_blueprint(user_blueprint)
app.register_blueprint(recipe_blueprint)
