from albient import app, db
from albient.models import User

with app.app_context():
    db.create_all()

    user = User(
        username="flyingseverus",
        email="sev@gmail.com",
        password="power",
        display_name="Sev",
    )
    user1 = User(
        username="pittan",
        email="pittan@gmail.com",
        password="power",
        display_name="Pittan",
    )
    user2 = User(
        username="srivathsa",
        email="srivathsa@gmail.com",
        password="power",
        display_name="Srivaths",
    )

    db.session.add_all([user, user1, user2])
    db.session.commit()
