from models.user_info import USER_INFO
from app.database.database import get_db,engine

from app.schemas import schemas
from sqlalchemy.orm import Session


class user_management(USER_INFO):
  
    def create_user(self, user_data):
        db = get_db()
        existing_user = db.query(USER_INFO).filter(
        (USER_INFO.user_email == user_data.user_email) | (USER_INFO.user_name == user_data.user_name)
    ).first()
        if existing_user:
            return ("Username or Email already registered")

        # Create new user
        new_user = USER_INFO(user_name=user_data.user_name, 
                             user_email=user_data.user_email,
                             user_password=user_data.user_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    @classmethod
    def get_user(self, user_email):
        # Logic to retrieve user information
        pass
    @classmethod
    def update_user(self, user_email, user_data):
        # Logic to update user information
        pass

    def delete_user(self, user_email):
        # Logic to delete a user
        pass
    def interal_test(self):
        return "This is an internal test method"

if __name__ == "__main__":
    ops = user_management()
    print(ops.interal_test())