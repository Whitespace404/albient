from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Length, EqualTo, DataRequired


class CreateUserForm(FlaskForm):
    username = StringField("Username", validators=[Length(max=64)])
    display_name = StringField("Display Name: ", validators=[Length(max=64)])
    password = PasswordField("Password", validators=[DataRequired(), Length(max=64)])
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), EqualTo("password", "Passwords do not match")],
    )

    submit = SubmitField()


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[Length(max=64)])
    password = PasswordField("Password", validators=[Length(max=64)])

    submit = SubmitField()
