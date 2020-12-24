from flask import Blueprint, url_for, render_template, flash, redirect
from auth_forms import AuthRegistrationForm, AuthLoginForm

auth_bp = Blueprint('auth_bp', __name__, template_folder = 'templates', static_folder = 'static', static_url_path = 'assets')


@auth_bp.route('/register', methods=["GET", "POST"])
def register():
    form = AuthRegistrationForm()
    #formhandling logic
    if form.validate_on_submit():
        flash('Account created',  'success')
        return redirect(url_for('main_bp.index'))
    return render_template('auth/register.html', form = form)


@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    form = AuthLoginForm()
    return render_template('auth/login.html', form = form)