from flask import Blueprint, url_for, render_template 

auth_bp = Blueprint('auth_bp', __name__, template_folder = 'templates', static_folder = 'static', static_url_path = 'assets')


@auth_bp.route('/register')
def register():
    return render_template('auth/register.html')


@auth_bp.route('/login')
def login():
    return render_template('auth/login.html')