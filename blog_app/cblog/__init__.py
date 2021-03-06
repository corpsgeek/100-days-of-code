from flask import Flask, Blueprint
#import main routes blueprint
from cblog.main.main_route import main_bp
from cblog.auth.auth_route import auth_bp
from cblog.user.user_route import user_bp
from cblog.posts.posts_route import post_bp



#importing init files to avoid circular imports
from cblog.auth import bcrypt, login_manager

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


#password manager 
bcrypt.init_app(app)
bcrypt.app = app 




#login manager feature initialization
login_manager.init_app(app)
login_manager.app = app
login_manager.login_view = 'auth_bp.login'
login_manager.login_message_category = 'info'

#register main blueprints
app.register_blueprint(main_bp, url_prefix='/')
app.register_blueprint(auth_bp, url_prefix='/')
app.register_blueprint(user_bp, url_prefix="/")
app.register_blueprint(post_bp, url_prefix="/")