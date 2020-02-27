from flask import Blueprint
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    print("@auth.route > login")
    return 'Login__xx'

@auth.route('/signup')
def signup():
    print("@auth.route > signup")
    return 'Signup__xx'

@auth.route('/logout')
def logout():
    print("@auth.route > logout")
    return 'Logout__xx'
