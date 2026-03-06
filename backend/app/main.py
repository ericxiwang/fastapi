from fastapi import FastAPI
import os
from app.config.config import Settings
from app.routers.user_router import user_router
from app.database.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine(Settings.DATABASE_URL)


app = FastAPI(title="User Management API", version="1.0")

@app.get("/")
async def root():
    return {"message": "Welcome to the User Management API!"}

# Include routers and dependency overrides
app.include_router(user_router)