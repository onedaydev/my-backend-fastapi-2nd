from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from domain.user import user_schema



router = APIRouter(
    prefix = "/api/user"
)


@router.post("/create", status_code = status.HTTP_204_NO_CONTENT)
async def create_user(
    user: user_schema.UserCreate, 
    db: Session = Depends(get_db)
    ):
    
    pass
    

