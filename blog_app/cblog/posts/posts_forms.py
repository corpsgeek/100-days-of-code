from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed

class PostForm(FlaskForm):
    title = StringField('Post Title', validators=[DataRequired()])
    content = TextAreaField('Post Content', validators=[DataRequired()])
    hero = FileField('Post Image', validators = [FileAllowed(['png', 'jpg', 'jpeg'])])
    publish = SubmitField('Publish')

   
