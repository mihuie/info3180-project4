from flask.ext.wtf import Form
from wtforms import validators
from wtforms.fields import StringField, IntegerField, SubmitField, FileField, SelectField, PasswordField
from wtforms.validators import Required, Length, NumberRange


class CreateUserForm(Form):
    username = StringField('Username', validators=[Length(min=4, max=25)])
    first_name = StringField('First Name', validators=[Length(min=4, max=25)])
    last_name = StringField('Last Name', validators=[Length(min=2, max=25)])
    password = PasswordField('New Password', validators=[Length(min=6), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')

    
class LoginForm(Form):
    username = StringField('Username', validators=[Length(min=4, max=25)])
    password = PasswordField('Password')