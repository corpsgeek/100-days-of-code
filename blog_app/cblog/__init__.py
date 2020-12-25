from flask import Flask, Blueprint
#import main routes blueprint
from cblog.main.main_route import main_bp
from cblog.auth.auth_route import auth_bp

#importing init files to avoid circular imports
from cblog.auth import bcrypt
from cblog.models import db   


app = Flask(__name__)
#load database
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///cblog.db'
#load configuration
app.config["SECRET_KEY"] = "0cbce54cd80f3448e3d5d6bf5a056731"


#initialize this init files of other component of the application
#import them also
db.init_app(app)
db.app = app    

bcrypt.init_app(app)
bcrypt.app = app 


#register main blueprints
app.register_blueprint(main_bp, url_prefix='/')
app.register_blueprint(auth_bp, url_prefix='/')