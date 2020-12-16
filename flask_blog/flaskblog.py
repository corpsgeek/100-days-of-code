from flask import Flask
from flask import render_template, flash, redirect, request, url_for
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SECRET_KEY'] = '58cc222d9a3993951da4cc75357b3f6d'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default='default.jpg')
    password = db.Column(db.String(60), nullable = False)

    def __repr__(self):
        return "User(" + str(self.username) + ',' + str(self.email) + ',' + str(self.image_file) + ")"

#TODO: Create post table





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


if __name__ == "__main__":
    app.run(debug=True) 