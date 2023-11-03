from sqlalchemy.orm import Session
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from passlib.context import CryptContext

from models import User

from domain.user.user_schema import UserCreate


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# C

def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, hashed_password = pwd_context.hash(user.password))
    db.add(db_user)
    db.commit()
    # db.refresh(db_user)
    return db_user

# R

def get_user(db: Session, user_create: UserCreate):
    return db.query(User).filter(User.email == user_create.email).first()


def get_user_by_email(db: Session, _email: str):
    return db.query(User).filter(User.email == _email).first()




# U

# D
