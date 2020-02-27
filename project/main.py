from flask import Blueprint
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    print("@main.route > /")
    return 'Index_xx'

@main.route('/profile')
def profile():
    print("@main.route > profile")
    return 'Profile_xx'
