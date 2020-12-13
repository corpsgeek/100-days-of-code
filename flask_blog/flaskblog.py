from flask import Flask
from flask import render_template

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)