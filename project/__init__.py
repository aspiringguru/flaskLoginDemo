from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    print("create_app():start__xx")
    app = Flask(__name__)

    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    #
    print("create_app():end__xx")
    return app
