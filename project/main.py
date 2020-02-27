from flask import Blueprint, render_template
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    print("@main.route > /")
    return render_template('index.html')


@main.route('/profile')
def profile():
    print("@main.route > profile")
    return render_template('profile.html')
