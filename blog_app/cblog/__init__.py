from flask import Flask, Blueprint
#import main routes blueprint
from cblog.main.main_route import main_bp
from cblog.auth.auth_route import auth_bp


app = Flask(__name__)

#register main blueprints
app.register_blueprint(main_bp, url_prefix='/')
app.register_blueprint(auth_bp, url_prefix='/')