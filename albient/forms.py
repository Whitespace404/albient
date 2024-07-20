from flask_wtf import FlaskForm

from wtforms import (StringField, 
                     SubmitField, 
                     PasswordField, 
                     SelectField, 
                     TextAreaField)


class CreateUserForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    confirm_password = PasswordField("Confirm Password")