from flask import Blueprint, render_template, render_template_string, request 
from .models import User
from . import db

main_bp = Blueprint('main', __name__)
user_bp = Blueprint('users', __name__, url_prefix='/user')


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    username = ''
    email = ''
    message = ''

    if request.method == 'POST':
        # Get the form data
        username = request.form.get('username')
        email = request.form.get('email')

        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        message = f'User {username} was saved successfully.'

    return render_template('index.html', message=message) 

@user_bp.route('/allusers')
def allusers():
    users = User.query.all()

    return render_template('users.html', users=users)
