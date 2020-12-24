from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import StringField, PasswordField, SubmitField


class AuthRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=5)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')]) 
    sign_up = SubmitField('Sign Up')

class AuthLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=5)])
    password = PasswordField('Password', validators=[DataRequired()])
    log_in = SubmitField('Log In')
