from pydantic import BaseModel


class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    
    # posts: list[Post] = []

    class Config:
        orm_mode = True

