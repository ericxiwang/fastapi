from fastapi import APIRouter, HTTPException,Depends
from app.models.user_info import USER_INFO
from app.database.database import get_db,engine
import sqlalchemy as db,select
from app.schemas import schemas
from sqlalchemy.orm import Session
from fastapi import Request

user_router = APIRouter(prefix="/users")


#USER_INFO.Base.metadata.create_all(bind=engine)
@user_router.post("/")
async def create_user(user_data):

    # In a real implementation, you would hash the password and interact with the database
    # Example: db = get_db(); new_user = create_user(db, user_data); return new_user
    return {"message": "User created successfully"}

@user_router.post("/new_user")
async def create_new_user(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    # In a real implementation, you would hash the password and interact with the database
    # Example: db = get_db(); new_user = create_user(db, user_data); return new_user
    return {"message": data}


@user_router.get("/all_users", response_model=list[schemas.UserRead])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(USER_INFO).all()
    return users
