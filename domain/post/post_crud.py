from datetime import datetime

from models import User, Post
from domain.post import post_schema
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


def get_post_list(db: Session,
                skip: int = 0,
                limit: int = 10,
                keyword: str = ''
    ):
    post_list = db.query(Post)
    if keyword:
        search = f"%%{keyword}%%"
        post_list = post_list.filter(Post.title.ilike(search) | 
                                     Post.content.ilike(search)
                                     )
    total = post_list.distinct().count()
    post_list = post_list.order_by(Post.create_date.desc()).offset(skip).limit(limit).distinct().all()

    return total, post_list


def get_post(db: Session, post_id: int):
    post = db.query(Post).get(post_id)
    return post


def update_post(db: Session, db_post: Post, post_update: post_schema.PostUpdate):
    db_post.title = post_update.title
    db_post.content = post_update.content
    db.add(db_post)
    db.commit()


def delete_post(db: Session, db_post: Post):
    db.delete(db_post)
    db.commit()