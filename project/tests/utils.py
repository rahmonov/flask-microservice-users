import datetime


from project import db
from project.api.models import User


def add_user(username, email, password, created_at=datetime.datetime.utcnow()):
    user = User(
        username=username,
        email=email,
        created_at=created_at,
        password=password,
    )
    db.session.add(user)
    db.session.commit()
    return user
