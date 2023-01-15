from sqlalchemy.orm import sessionmaker

from database import engine
import schemas
import models

models.Base.metadata.create_all(bind=engine)


def get_user_by_id(user_id: int):
    db = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = db()
    user = session.query(models.User).filter(models.User.id == user_id).first()
    return user


def add_user(user: schemas.User):
    db = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = db()
    db_user = models.User(login=user.login, email=user.email, phone=user.phone)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
