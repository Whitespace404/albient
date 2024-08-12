from albient import db, login_manager
from flask_login import UserMixin
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class User(db.Model, UserMixin):
    id = sa.Column(sa.Integer, primary_key=True, unique=True)
    email = sa.Column(sa.String(320))
    username = sa.Column(sa.String(64), nullable=False, unique=True)
    display_name = sa.Column(sa.String(32))
    password = sa.Column(sa.String(64), nullable=False)

    rep_points = sa.Column(sa.Integer)
    questions = relationship("Question", backref="op", lazy=True)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Question(db.Model):
    id = sa.Column(sa.Integer, primary_key=True, unique=True)
    title = sa.Column(sa.String(64))
    content = sa.Column(sa.Text)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"))
