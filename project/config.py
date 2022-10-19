import os


class Baseconfig:
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    TOP_LEVEL_DIR = os.path.abspath(os.curdir)

    SECRET_KEY = 'Sccl3OozBp'
    DEBUG = True

    # SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    WTF_CSRF_ENABLED = True
