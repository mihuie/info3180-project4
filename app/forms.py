from flask.ext.wtf import Form
from wtforms import validators
from wtforms.fields import StringField, IntegerField, SubmitField, FileField, SelectField, PasswordField
from wtforms.validators import Required, Length, NumberRange
from wtforms.fields.html5 import EmailField


class CreateUserForm(Form):
    username = StringField('Username', validators=[Length(min=4, max=25)])
    first_name = StringField('First Name', validators=[Length(min=4, max=25)])
    last_name = StringField('Last Name', validators=[Length(min=2, max=25)])
    password = PasswordField('New Password', validators=[Length(min=6), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    age = IntegerField('Age', validators=[NumberRange(min=16, max=99)])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('Female','Female')])    
    image = FileField('Image File', validators=[Required()])
    email = EmailField('Email address', [validators.DataRequired(), validators.Email()])
    

    
class LoginForm(Form):
    username = StringField('Username', validators=[Length(min=4, max=25)])
    password = PasswordField('Password')