from flask import Blueprint, render_template, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from cblog.user.user_forms import UserProfileForm
from cblog.models import db, User, Post, Comment
from cblog.auth import bcrypt 
user_bp = Blueprint('user_bp', __name__, template_folder = 'templates', static_folder = 'static')


@user_bp.route("/profile", methods=["POST", "GET"])
@login_required
def profile():
    form = UserProfileForm()
        
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data 
        #encrypt password
        new_encrypted_password = bcrypt.generate_password_hash(form.password.data)  
        current_user.password = new_encrypted_password
        
        #comit changes to db 
        db.session.commit()
    elif request.method == "GET":
        form.username.data = current_user.username 
        form.email.data = current_user.email
    return render_template('user_profile.html', form = form)
