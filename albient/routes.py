from albient import app
from flask import render_template


@app.route("/home")
@app.route("/")
def home():
    ish = [
        ["What is 1+1", "I am not having the clarity in the maths you know what is 1+1 is"],
        ["how to do crosss aldol addiotn", 'ethanal']
    ]
    return render_template("home.html", questions=ish)


@app.route("/login")
def login():
    return "<h1> login </h1>"
