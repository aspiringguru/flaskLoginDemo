from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    print("@auth.route > login")
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    print("@auth.route > /login > def login_post()")
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    print("email:", email)
    print("password:", password)
    print("remember:", remember)
    user = User.query.filter_by(email=email).first()
    print("after checking match in database, user:", user)
    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password):
        print("user and password match - failed.")
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page
    else:
        print("user and password match - OK, redir to profile")
    print("now flask_login.login_user with user="+str(user)+", and remember="+str(remember))
    login_user(user, remember=remember)
    # if the above check passes, then we know the user has the right credentials
    return redirect(url_for('main.profile'))

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
