from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required, login_user, logout_user

from albient import app, db
from albient.forms import LoginForm, CreateUserForm, CreatePostForm, ReplyPostForm
from albient.models import User, Question, Comment


@app.route("/home")
@app.route("/")
def home():
    questions = Question.query.order_by(Question.id.desc()).all()
    return render_template("home.html", questions=questions)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() # .first(), .all(), .last()
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


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out")
    return redirect(url_for("home"))


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


@app.route("/ask", methods=["GET", "POST"])
@login_required
def ask():
    form = CreatePostForm()
    if form.validate_on_submit():
        question = Question(title=form.title.data, content=form.content.data, op=current_user, tags=form.tags.data)
        db.session.add(question)
        db.session.commit()

        flash("Question posted")
        return redirect(url_for("home"))
    return render_template("create_post.html", form=form, title="Ask A Question")


@app.route("/view_question", methods=["GET", "POST"])
def view_question():
    post_id = request.args.get("id")
    question = Question.query.filter_by(id=post_id).first()
    assert question is not None
    replies = Comment.query.filter_by(question=question).all()

    form = ReplyPostForm()

    if form.validate_on_submit():
        reply = Comment(content=form.content.data, question=question, op=current_user)
        db.session.add(reply)
        db.session.commit()
        flash("Reply added")
        return redirect(url_for('view_question', id=question.id))
    return render_template("view_question.html", form=form, title="Reply", question=question, replies=replies)


@app.route("/view_user/<username>")
def view_user(username):
    user = User.query.filter_by(username=username).first()

    qa = Question.query.filter_by(op=user).all()
    questions_asked = len(qa)

    votes = sum([i.votes for i in qa])

    answers = len(Comment.query.filter_by(op=user).all())

    return render_template(
        "view_user.html", user=user, qa=questions_asked, votes=votes, answers=answers
    )


@app.route("/upvote_post/<post_id>")
def upvote_post(post_id):
    post = Question.query.filter_by(id=post_id).first()
    post.votes += int(request.args.get("del"))
    db.session.add(post)
    db.session.commit()
    return redirect(request.referrer)


@app.route("/upvote_comment/<comment_id>")
def upvote_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()
    comment.votes += int(request.args.get("del"))
    db.session.add(comment)
    db.session.commit()
    return redirect(request.referrer)
