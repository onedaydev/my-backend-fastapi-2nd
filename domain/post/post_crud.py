from datetime import datetime

from models import User, Post
from domain.post import post_schema
from domain.user import user_schema
from sqlalchemy.orm import Session


def create_post(db: Session, post_create: post_schema.PostCreate, user: User):
    db_post = Post(
        title = post_create.title,
        content = post_create.content,
        create_date = datetime.now(),
        owner = user
    )
    db.add(db_post)
    db.commit()


