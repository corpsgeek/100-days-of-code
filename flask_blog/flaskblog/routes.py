from flask import render_template, flash, redirect, request, url_for
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User,Posts 
from flaskblog import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        #user authentication logic
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash('Your account has been created', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Registration', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
     
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
                flash('Welcome user', 'success')
            else:
                flash('Welcome user', 'success')
                return redirect(url_for('home'))
        else:
            flash('Login Unsuccesful, check email and password', 'danger')
    return render_template('login.html', title='Log in', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title = 'account')