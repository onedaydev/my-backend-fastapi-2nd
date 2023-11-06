# from typing import Annotated

# from datetime import timedelta, datetime

from fastapi import Depends, APIRouter, status, HTTPException

from sqlalchemy.orm import Session

from dependencies import get_db

from domain.post import post_schema, post_crud
from domain.user import user_schema, user_crud, user_router

router = APIRouter(
    prefix="/posts",
    tags= ["posts"],
)

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def posts_create(_post_create: post_schema.PostCreate,
                db: Session = Depends(get_db),
                current_user: user_schema.User = Depends(user_router.get_current_active_user)):
    post_crud.create_post(db, _post_create, user=current_user)

