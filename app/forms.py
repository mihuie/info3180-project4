from flask.ext.wtf import Form
from wtforms import validators
from wtforms.fields import StringField, IntegerField, SubmitField, FileField, SelectField, PasswordField
from wtforms.validators import Required, Length, NumberRange, Optional
from wtforms.fields.html5 import EmailField


class CreateUserForm(Form):
    password = PasswordField('New Password', validators=[Length(min=6), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    email = EmailField('Email address', [validators.DataRequired(), validators.Email()])

class LoginForm(Form):
    email = EmailField('Email Address', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password')
    
class EditForm(Form):
    username = StringField('Username', validators=[Length(min=4, max=25)])
    first_name = StringField('First Name', validators=[Length(min=4, max=25)])
    last_name = StringField('Last Name', validators=[Length(min=2, max=25)])
    age = IntegerField('Age', validators=[NumberRange(min=16, max=99)])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('Female','Female')])    
    email = EmailField('Email Address', [validators.DataRequired(), validators.Email()])
    
class changePWForm(Form):
    current = PasswordField('Current Password', [validators.DataRequired()])
    password = PasswordField('New Password', validators=[Length(min=6), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')

class photoForm(Form):
    image = FileField('Profile Picture', [validators.DataRequired()])   
