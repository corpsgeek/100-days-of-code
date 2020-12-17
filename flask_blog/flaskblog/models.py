from flaskblog import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default='default.jpg')
    password = db.Column(db.String(60), nullable = False)
    post = db.relationship('Posts', backref='author', lazy=True)
    

    def __repr__(self):
        return "User(" + str(self.username) + ',' + str(self.email) + ',' + str(self.image_file) + ")"


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    content = db.Column(db.Text, nullable = False)
    dateposted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable= False)

    def __repr__(self):
            return "User(" + str(self.title) + ',' + str(self.dateposted) + ")"