from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
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

@auth.route('/signup', methods=['POST'])
def signup_post():
    print("@auth.route method=POST > signup_post")
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    print("email:", email)
    print("name:", name)
    print("password:", password)
    user = User.query.filter_by(email=email).first()
    print("result of database query, user=", user)
    # if this returns a user, then the email already exists in database
    if user: # if a user is found, we want to redirect back to signup page so user can try again
        print("user found in database. redirecting")
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    else:
        print("user not found, creating.")
    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    print("user added to database and committed, redirecting.")
    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    print("@auth.route > logout")
    return 'Logout__xx'
