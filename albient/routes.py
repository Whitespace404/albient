from albient import app
from flask import render_template


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return "<h1> login </h1>"
