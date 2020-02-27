from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    print("@main.route > /")
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    print("@main.route > profile, name=",current_user.name)
    return render_template('profile.html', name=current_user.name)
