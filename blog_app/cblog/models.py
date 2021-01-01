#db imports
from flask_sqlalchemy import SQLAlchemy
from cblog.auth import login_manager
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

#user loader required
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# database User table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    # has relationship with posts
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        return "User(" + str(self.username) + ',' + str(self.email) +")"


# database Post table
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    dateposted = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    image = db.Column(db.String, nullable=False, default='default.jpg')
    clicks = db.Column(db.Integer, nullable=True, default=0)
    # create a virtual column in the user table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    #create a virtual column in the comment table
    comment_id = db.relationship('Comment', backref='commentary', lazy = True) 

    def __repr__(self):
        return "User(" + str(self.title) + ',' + str(self.dateposted) +")"


#database comments table
class Comment(db.Model):
    id = db.Column(db.String, primary_key = True)
    name =  db.Column(db.String, nullable = False)
    message = db.Column(db.Text, nullable = False)
    #comment has relationship with posts
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable= False)

    def __repr__(self):
        return "User(" + str(self.name) + ',' + str(self.message) +")"

