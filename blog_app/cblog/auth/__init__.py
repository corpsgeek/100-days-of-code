# import the extensions needed for this blueprint 
# in its init file. this avoids circular import issues 
# then in the main application init file, we import this files init package there


#import password encryption
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt()


#import login manager
from flask_login import LoginManager
login_manager = LoginManager()