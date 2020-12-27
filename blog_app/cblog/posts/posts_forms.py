from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class PostForm(FlaskForm):
    title = StringField('Post Title', validators=[DataRequired()])
    content = TextAreaField('Post Content', validators=[DataRequired()])
    publish = SubmitField('Publish')

   
