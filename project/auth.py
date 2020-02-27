from flask import Blueprint, render_template
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    print("@auth.route > login")
    return render_template('login.html')

@auth.route('/signup')
def signup():
    print("@auth.route > signup")
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    print("@auth.route > logout")
    return 'Logout__xx'
