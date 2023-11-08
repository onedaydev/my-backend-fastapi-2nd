# from typing import Annotated

# from datetime import timedelta, datetime
from fastapi import Depends, APIRouter, status, HTTPException

from sqlalchemy.orm import Session

from dependencies import get_db

from domain.post import post_schema, post_crud
from domain.user import user_schema, user_router

router = APIRouter(
    prefix="/post",
    tags= ["posts"],
)

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def posts_create(_post_create: post_schema.PostCreate,
                db: Session = Depends(get_db),
                current_user: user_schema.User = Depends(user_router.get_current_active_user)):
    post_crud.create_post(db, _post_create, user=current_user)

@router.get("/list", response_model=post_schema.PostList)
def post_list(db: Session = Depends(get_db),
              page: int=0, limit: int = 10, keyword: str = ''
              ):
    total, post_list = post_crud.get_post_list(
        db=db, skip = page * limit, limit=limit, keyword=keyword
    )
    return {'total': total, 
        'post_list': post_list        
    }


@router.get("/detail/{post_id}", response_model=post_schema.Post)
def post_detail(post_id: int, db: Session = Depends(get_db)):
    post = post_crud.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="데이터를 찾을 수  없습니다.")
    return post

@router.put("/update", status_code=status.HTTP_204_NO_CONTENT)
def post_update(_post_update: post_schema.PostUpdate,
                    db: Session = Depends(get_db),
                    current_user: user_schema.User = Depends(user_router.get_current_active_user)):
    db_post= post_crud.get_post(db, _post_update.post_id)
    if not db_post:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_post.owner.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="수정 권한이 없습니다.")
    post_crud.update_post(db, db_post, _post_update)

@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def post_delete(_post_delete: post_schema.PostDelete,
                    db: Session = Depends(get_db),
                    current_user: user_schema.User = Depends(user_router.get_current_active_user)):
    db_post = post_crud.get_post(db, post_id=_post_delete.post_id)
    if not db_post:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_post.owner.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="삭제 권한이 없습니다.")
    post_crud.delete_post(db, db_post)
