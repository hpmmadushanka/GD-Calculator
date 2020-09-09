from flask_wtf import FlaskForm
from wtforms.widgets import TextArea
from wtforms.fields import TextAreaField, MultipleFileField
from wtforms import StringField, PasswordField, BooleanField

from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=3, max=15)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=3, max=15)])

class ProjectForm(FlaskForm):
    projectName = StringField('Project Name', validators=[InputRequired(), Length(min=5, max=30)])
    projectDescription = TextAreaField('Project Description', validators=[Length(min=0, max=200)])
    files = MultipleFileField('test files', validators=[InputRequired()])