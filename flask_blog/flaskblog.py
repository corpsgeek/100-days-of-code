from flask import Flask
from flask import render_template
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '58cc222d9a3993951da4cc75357b3f6d'
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

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Registration', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Log in', form=form)


if __name__ == "__main__":
    app.run(debug=True)