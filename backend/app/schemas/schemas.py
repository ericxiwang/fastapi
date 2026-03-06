from pydantic import BaseModel, EmailStr

class UserRead(BaseModel):
    id: int
    user_name: str
    user_email: EmailStr

    class Config:
        orm_mode = True