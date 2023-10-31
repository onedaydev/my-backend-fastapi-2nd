from datetime import datetime, timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException,status
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic import BaseModel

# openssl rand -hex 32
SECRET_KEY = "2431cef98507f58611d5fcfac707a585af107f47388f614c4916db50f6a32fa3"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/users",
    tags=['users'],
)

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def user_create(_user_create ,db):
    pass

@router.post("/login", response_model=Token)
def user_login():
    pass


@router.put("/change_pwd", response_model=None)
def change_pwd():
    pass

@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def delete_user():
    pass
