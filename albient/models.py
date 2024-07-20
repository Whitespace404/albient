from albient import db
import sqlalchemy as sa
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = "User"
    id = sa.Column(sa.Integer, primary_key=True, unique=True)
    username = sa.Column(sa.String(64), nullable=False, unique=True)
    display_name = sa.Column(sa.String(32))
    password = sa.Column(sa.String(64), nullable=False)

    rep_points = sa.Column(sa.Integer)
    questions = relationship("Question", backref="op", lazy=True)
    

class Question(db.Model):
    id = sa.Column(sa.Integer, primary_key=True, unique=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"))
    title = sa.Column(sa.String(64))
    content = sa.Column(sa.BLOB)
