from typing import Optional

from pydantic import BaseModel, EmailStr

class UserRead(BaseModel):
    id: int
    user_name: str
    user_email: EmailStr
    user_password: str
    user_group: int
    user_description: str | None = None



class UserCreate(BaseModel):
    user_name: str
    user_email: EmailStr
    user_password: str
    user_group: int
    user_description: str | None = None

class UserUpdate(BaseModel):
    user_name: Optional[str] = None
    user_password: Optional[str] = None
    user_group: Optional[int] = None
    user_description: Optional[str] = None