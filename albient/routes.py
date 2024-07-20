from flask import render_template

from albient import app
from albient.forms import LoginForm, CreateUserForm


@app.route("/home")
@app.route("/")
def home():
    ish = [
        [
            "What is 1+1",
            "I am not having the clarity in the maths you know what is 1+1 is",
        ],
        ["how to do crosss aldol addiotn", "ethanal"],
    ]
    return render_template("home.html", questions=ish)


@app.route("/login")
def login():
    return "<h1> login </h1>"


@app.route("/register", methods=["GET", "POST"])
def register():
    form = CreateUserForm()
    if form.validate_on_submit:
        print(form.username.data)
        print(form.password.data)
    return render_template("register.html", form=form)
