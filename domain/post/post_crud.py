from datetime import datetime

from models import User, Post
from domain.post import post_schema
from domain.user import user_schema
from sqlalchemy.orm import Session

# C

def create_post(db: Session, post_create: post_schema.PostCreate, user: User):
    db_post = Post(
        title = post_create.title,
        content = post_create.content,
        create_date = datetime.now(),
        owner = user
    )
    db.add(db_post)
    db.commit()

# R

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

# U

# D