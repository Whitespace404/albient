from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required, login_user, logout_user

from albient import app, db
from albient.forms import LoginForm, CreateUserForm
from albient.models import User


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


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash("Incorrect username/password", "alert")
        elif form.password.data == user.password:
            login_user(user)
            flash(f"Logged in")
            next_page = request.args.get("next")
            return redirect(next_page if next_page else url_for("home"))
        else:
            flash("Incorrect username/password", "alert")
            return redirect(url_for("login"))
    return render_template("login.html", form=form, title="Login")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = CreateUserForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            display_name=form.display_name.data,
        )
        db.session.add(user)
        db.session.commit()

        flash(f"{user.username} registered successfully.")
        return redirect(url_for("login"))
    return render_template("register.html", form=form, title="Register")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out")
    return redirect(url_for("home"))
