from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "m15mtwtmwlhsmm_aw3W5akn6aGpZf3Tp10"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"

db = SQLAlchemy(app)
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = "login"

from albient import routes
