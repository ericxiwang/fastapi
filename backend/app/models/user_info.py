from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class USER_INFO(Base):
    __tablename__ = 'USER_INFO'
    id = Column(Integer, primary_key=True)
    user_email = Column(String, unique=True, nullable=False)
    user_password = Column(String, nullable=False)
    user_name = Column(String, nullable=False)
    user_group = Column(String)



