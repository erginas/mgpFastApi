from pydantic import BaseModel
from typing import Optional

class UsersBase(BaseModel):
    id: Optional[String] = None
    email: Optional[String] = None
    full_name: Optional[String] = None
    password: Optional[String] = None
    is_active: Optional[String] = None
    created_at: Optional[DateTime] = None
    updated_at: Optional[DateTime] = None
    articles: Optional[Integer] = None
    title: Optional[String] = None
    profile_path: Optional[String] = None

class UsersCreate(UsersBase):
    pass

class Users(UsersBase):
    id: Optional[int]

    class Config:
        orm_mode = True