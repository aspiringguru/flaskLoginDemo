from flask import Blueprint, render_template, session
from flask_login import login_required, current_user
from . import db
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    print("@main.route > /")
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    print("@main.route > profile, name=",current_user.name)
    messages = session['messages']
    print("@main.route > profile, messages=",messages)
    return render_template( 'profile.html',
                            name=current_user.name,
                            email=current_user.email,
                            messages=json.loads(messages))
