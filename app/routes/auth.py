from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import User
from app.schemas import UserCreate
from app.utils.auth import hash_password, create_access_token
from sqlalchemy import text
router = APIRouter()

@router.post("/register")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    hashed_pwd = hash_password(user.password)
    new_user = User(username=user.username, hashed_password=hashed_pwd)
    #print("hello")
    db.add(new_user)
    await db.commit()
    return {"message": "User registered successfully"}

@router.post("/login")
async def login(user: UserCreate, db: AsyncSession = Depends(get_db)):
    query = await db.execute(text("SELECT * FROM users WHERE username=:username"), {'username': user.username})
    db_user = query.fetchone()
    if not db_user or not hash_password(user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token({"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}
