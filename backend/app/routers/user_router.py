from fastapi import APIRouter, HTTPException,Depends
from app.models.user_info import USER_INFO
from app.database.database import get_db,engine
from app.schemas import schemas
from sqlalchemy.orm import Session


user_router = APIRouter(prefix="/users")


#USER_INFO.Base.metadata.create_all(bind=engine)
@user_router.post("/")
async def test(user_data: schemas.UserUpdate):

    # In a real implementation, you would hash the password and interact with the database
    # Example: db = get_db(); new_user = create_user(db, user_data); return new_user
    return {"message": "test", "user_data": user_data}

@user_router.get("/all-users", response_model=list[schemas.UserRead])
async def get_all_users(db: Session = Depends(get_db)):
    users = db.query(USER_INFO).all()
    return users

@user_router.post("/create-user")
async def create_new_user(user_info: schemas.UserCreate, db: Session = Depends(get_db)):
    duplicate_user = db.query(USER_INFO).filter(USER_INFO.user_email == user_info.user_email).first()
    if duplicate_user:
        raise HTTPException(status_code=400, detail="Email already exists") 
    
    new_user = USER_INFO(
        user_name=user_info.user_name,
        user_email=user_info.user_email,
        user_password=user_info.user_password,
        user_group=user_info.user_group,
        user_description=user_info.user_description
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@user_router.get("/get-user/{user_email}", response_model=schemas.UserCreate)
async def get_user_by_email(user_email: str, db: Session = Depends(get_db)):
    user = db.query(USER_INFO).filter(USER_INFO.user_email == user_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.delete("/delete-user/{user_email}")
async def delete_user_by_email(user_email: str, db: Session = Depends(get_db)):
    user = db.query(USER_INFO).filter(USER_INFO.user_email == user_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"} 

@user_router.patch("/update-user/{user_email}")
async def update_user_by_email(user_email: str, updated_info: schemas.UserUpdate, db: Session = Depends(get_db)):
    user = db.query(USER_INFO).filter(USER_INFO.user_email == user_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    updated_info = updated_info.model_dump(exclude_unset=True)

    for key, value in updated_info.items():
        setattr(user, key, value)
    
    db.commit()
    db.refresh(user)
    return user


