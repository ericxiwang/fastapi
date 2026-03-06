from pydantic import BaseModel, EmailStr

class UserRead(BaseModel):
    id: int
    user_name: str
    user_email: EmailStr
    user_password: str
    user_description: str | None = None


    class Config:
        orm_mode = True