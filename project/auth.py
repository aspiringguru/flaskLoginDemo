from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User, LogonHistory
from . import db
from datetime import datetime
import json

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
    remoteip = request.remote_addr
    print("email:", email)
    print("password:", password)
    print("remember:", remember)
    print("remoteip:", remoteip)
    user = User.query.filter_by(email=email).first()
    last_login = LogonHistory.query.filter_by(email=email, success=True).order_by(LogonHistory.date.desc()).first() #.limit(5).all()
    if last_login:
        print("last_login:", last_login)
        print("type(last_login):", type(last_login))
        print("last_login:", last_login,
                    last_login.user_id,
                    last_login.email,
                    last_login.ipaddress,
                    last_login.success,
                    last_login.date)
        last_failed_login = LogonHistory.query.filter_by(email=email, success=False).filter(LogonHistory.date>last_login.date).order_by(LogonHistory.date.desc()).limit(5).all()
        if last_failed_login:
            print("last_failed_login:", last_failed_login)
            print("len(last_failed_login):", len(last_failed_login))
    else:
        print("No previous login attempts for email=", email)
    print("user found in database by email, user:"+str(user))
    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    # werkzeug.security.check_password_hash
    if not user or not check_password_hash(user.password, password):
        print("user and password match - failed.")
        flash('Please check your login details and try again.')
        #user_id, email, ipaddress, success, date
        new_login_attempt = LogonHistory(user_id=None, email=email, ipaddress=remoteip, success=False, date=datetime.now())
        # add the new user to the database
        db.session.add(new_login_attempt)
        db.session.commit()
        return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page
    else:
        print("user and password match - OK, redir to profile, user:"+str(user) +", user.id:"+str(user.id))
    print("now flask_login.login_user with user="+str(user)+", and remember="+str(remember))
    print("user.id:", user.id)
    #record successful login in database.
    new_login_attempt = LogonHistory(user_id=user.id, email=email, ipaddress=remoteip, success=True, date=datetime.now())
    # add the new user to the database
    db.session.add(new_login_attempt)
    db.session.commit()
    #now get count of unsuccessful logins.
    failed_login_count=0
    #flask_login.login_user
    #, failed_login_count=failed_login_count
    login_user(user, remember=remember)
    # if the above check passes, then we know the user has the right credentials
    num_failed_logins_since_last_login = len(last_failed_login)
    print("num_failed_logins_since_last_login=", num_failed_logins_since_last_login)
    if num_failed_logins_since_last_login>0:
        print("num_failed_logins_since_last_login>0")

    temp = str(last_login.date.strftime("%d/%b/%Y, %H:%M:%S"))
    print("last_login.date = ", str(temp))
    messages = json.dumps({"last_login_date":temp, "num_failed_logins_since_last_login":num_failed_logins_since_last_login })
    session['messages'] = messages
    #possibly move this up to lock account if x failed logins since last valid login.
    num_failed_logins_since_last_login = len(last_failed_login)
    print("num_failed_logins_since_last_login=", num_failed_logins_since_last_login)
    if num_failed_logins_since_last_login>0:
        print("num_failed_logins_since_last_login>0")
        session['num_failed_logins_since_last_login'] = num_failed_logins_since_last_login
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
@login_required
def logout():
    print("@auth.route > logout")
    logout_user()
    return redirect(url_for('main.index'))
