from flask import Blueprint, url_for, render_template, flash, redirect
from cblog.auth.auth_forms import AuthRegistrationForm, AuthLoginForm 
from cblog.models import db, User, Post, Comment 
from cblog.auth import bcrypt

auth_bp = Blueprint('auth_bp', __name__, template_folder = 'templates', static_folder = 'static', static_url_path = 'assets')


@auth_bp.route('/register', methods=["GET", "POST"])
def register():
    form = AuthRegistrationForm()
   
    if form.validate_on_submit():
        #encrypt the password
        encrypted_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password = encrypted_password)
        #commit the form data to db
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully', 'success')
        return redirect(url_for('auth_bp.login'))

    return render_template('auth/register.html', form = form)


@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    form = AuthLoginForm()
   
    return render_template('auth/login.html', form = form)