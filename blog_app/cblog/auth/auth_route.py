from flask import Blueprint, url_for, render_template, flash, redirect, request
from cblog.auth.auth_forms import AuthRegistrationForm, AuthLoginForm 
from cblog.models import db, User, Post, Comment 
from cblog.auth import bcrypt
from flask_login import login_user, current_user, logout_user, login_required

auth_bp = Blueprint('auth_bp', __name__, template_folder = 'templates', static_folder = 'static', static_url_path = 'assets')


@auth_bp.route('/register', methods=["GET", "POST"])
def register():
    #if user nav and is authenticated redirect to home page
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.home'))

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
    #if user nav and is authenticated redirect to home page
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.index'))

    form = AuthLoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            #fetch next page url from next page 
            next_page = request.args.get('next')
            #logic if user access a page without being logged in
            if next_page:
                return redirect(next_page)
                flash('Welcome user', 'success')
            else:
                return redirect(url_for('main_bp.index'))
                flash('Welcome to coffee hub', 'success')
           
         
        else:
            flash('Login unsuccessful', 'danger')

    return render_template('auth/login.html', form = form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main_bp.index'))

@auth_bp.route('/profile')
@login_required
def profile():
   
    return "user profile"