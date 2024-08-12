from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, TextAreaField
from wtforms.validators import Length, EqualTo, DataRequired


class CreateUserForm(FlaskForm):
    username = StringField("Username", validators=[Length(max=64)])
    display_name = StringField("Display Name: ", validators=[Length(max=64)])
    email = EmailField("Email", validators=[DataRequired(), Length(max=64)])
    password = PasswordField("Password", validators=[DataRequired(), Length(max=64)])
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), EqualTo("password", "Passwords do not match")],
    )

    submit = SubmitField()


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[Length(max=64)])
    password = PasswordField("Password", validators=[Length(max=64)])

    submit = SubmitField()


class CreatePostForm(FlaskForm):
    title = StringField("Title", validators=[Length(max=31)])
    content = TextAreaField()
    submit = SubmitField()
