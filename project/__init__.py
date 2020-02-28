from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
print("__init__.py, db=", db)

def create_app():
    print("create_app():start__xx")
    app = Flask(__name__)

    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #app.config['SERVER_NAME']="127.0.0.1:5000"#do not use causes problems?
    #nbb: this is how we set port export FLASK_RUN_PORT=8000

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table,
        # use it in the query for the user
        print("__init.py > @login_manager.user_loader > load_user(user_id), user_id="+ str(user_id))
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    #
    print("create_app():end__xx")
    return app


print("db.create_all start")
db.create_all(app=create_app())
print("db.create_all completed")
