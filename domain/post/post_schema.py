from pydantic import BaseModel, validator
import datetime

class Post(BaseModel):
    id: int
    title: str
    content: str
    create_date: datetime.datetime
    owner_id: int

    class Config:
        orm_mode = True

class PostCreate(BaseModel):
    title: str
    content: str

    @validator("title", "content")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("Null Value Error")
        return v

