from albient import db, login_manager
from flask_login import UserMixin
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class User(db.Model, UserMixin):
    id = sa.Column(sa.Integer, primary_key=True, unique=True)

    role_id = sa.Column(sa.Integer, default=0)  # 0 for normal users, 1 for admin

    email = sa.Column(sa.String(320))
    username = sa.Column(sa.String(64), nullable=False, unique=True)
    display_name = sa.Column(sa.String(32))
    password = sa.Column(sa.String(64), nullable=False)

    rep_points = sa.Column(sa.Integer)

    questions = relationship("Question", backref="op", lazy=True)
    replies = relationship("Comment", backref="op", lazy=True)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Question(db.Model):
    id = sa.Column(sa.Integer, primary_key=True, unique=True)
    title = sa.Column(sa.String(64))
    content = sa.Column(sa.Text)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"))
    comments = relationship("Comment", backref="question", lazy=True)
    tags = sa.Column(sa.String(32))
    votes = sa.Column(sa.Integer, default=0)
    is_resolved = sa.Column(sa.Boolean, default=False)


class Comment(db.Model):
    id = sa.Column(sa.Integer, primary_key=True, unique=True)
    content = sa.Column(sa.Text)
    votes = sa.Column(sa.Integer, default=0)
    question_id = sa.Column(sa.Integer, sa.ForeignKey("question.id"))
    user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"))


class Vote(db.Model):
    id = sa.Column(sa.Integer, primary_key=True, unique=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"))
    post_id = sa.Column(sa.Integer, sa.ForeignKey("question.id"), nullable=True)
    comment_id = sa.Column(sa.Integer, sa.ForeignKey("comment.id"), nullable=True)
    value = sa.Column(sa.Integer)  # +1 for upvote, -1 for downvote

    __table_args__ = (
        sa.UniqueConstraint("user_id", "post_id", name="unique_user_post_vote"),
        sa.UniqueConstraint("user_id", "comment_id", name="unique_user_comment_vote"),
    )
