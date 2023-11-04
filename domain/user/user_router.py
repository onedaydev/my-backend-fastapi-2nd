from typing import Annotated
from datetime import timedelta, datetime

from fastapi import Depends, APIRouter, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from jose import jwt, JWTError

from sqlalchemy.orm import Session

from dependencies import get_db
from domain.user import user_schema, user_crud
from domain.user.user_crud import pwd_context

from config import settings

ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM


router = APIRouter(
    prefix = "/user",
    tags = ["user"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")

@router.post("/create", status_code = status.HTTP_204_NO_CONTENT)
async def create_user(
    _user_create: user_schema.UserCreate, 
    db: Session = Depends(get_db)
    ):
    user = user_crud.get_user(db,_user_create)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="email 중복")
    user_crud.create_user(db,_user_create)


@router.post("/login", response_model=user_schema.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(),
            db: Session = Depends(get_db)):
    user = user_crud.get_user_by_email(db, form_data.username)
    if not user or not pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect email or password', headers={"WWW-Authenticate": "Bearer"},
        )
    data = {
        "sub": user.email,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": access_token, "token_type": "bearer"}


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate":"Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = user_schema.TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = user_crud.get_user_by_email(db, token_data.email)
    if user is None:
        raise credentials_exception
    return user



async def get_current_active_user(current_user: Annotated[str, Depends(get_current_user)],
    db: Session = Depends(get_db)
    ):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.get("/me")
async def read_users_me(current_user: Annotated[user_schema.User, Depends(get_current_active_user)]):
    return current_user

