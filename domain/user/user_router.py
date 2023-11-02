from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from domain.user import user_schema, user_crud


router = APIRouter(
    prefix = "/api/user",
    tags = ["user"],
)


@router.post("/create", status_code = status.HTTP_204_NO_CONTENT)
async def create_user(
    _user_create: user_schema.UserCreate, 
    db: Session = Depends(get_db)
    ):
    user = user_crud.get_user(db,_user_create)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="email 중복")
    user_crud.create_user(db,_user_create)

