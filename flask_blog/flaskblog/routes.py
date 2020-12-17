from flask import render_template, flash, redirect, request, url_for
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User,Posts 
from flaskblog import app

posts = [
    {
        'author': 'Boora',
        'title':  'My first blog post',
        'content': 'THis is my first post content',
        'date_posted': 'april 10,2019'
    },
    {
        'author': 'Peter',
        'title':  'My peter blog post',
        'content': 'THis is my peter post content',
        'date_posted': 'april 22,2019'
    },
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for' + form.username.data + '!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Registration', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@xyz.com" and form.password.data == "password":
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed', 'danger')
        
    return render_template('login.html', title='Log in', form=form)

