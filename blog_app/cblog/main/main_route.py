#import flask blueprint and render template
from flask import Blueprint, render_template, url_for

#initialize blueprint, declaring template and static folder
#set static url path as assets
main_bp = Blueprint('main_bp', __name__, template_folder = 'templates', static_folder = 'static', static_url_path = 'assets')

@main_bp.route('/')
def index():
    return render_template('main/home.html')

@main_bp.route('/about')
def about():
    return render_template('main/about.html')

@main_bp.route('/gallery')
def gallery():
    return render_template('main/gallery.html')


@main_bp.route('/contact')
def contact():
    return render_template('main/contact.html')