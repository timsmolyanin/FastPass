# app/routers/auth.py

from fastapi import APIRouter, HTTPException
from schemas import UserCreate, UserLogin
import os


router = APIRouter()

USERS_DB = {}  # Простое хранилище пользователей для примера

@router.post("/register")
def register_user(user: UserCreate):
    """
    Регистрирует нового пользователя.
    """
    if user.username in USERS_DB:
        raise HTTPException(status_code=400, detail="Username already registered")
    USERS_DB[user.username] = {"master_password": user.master_password}
    # Создаем директорию для хранения паролей пользователя
    os.makedirs(os.path.join("passwords", user.username), exist_ok=True)
    return {"message": "User registered successfully"}

@router.post("/login")
def login_user(user: UserLogin):
    """
    Аутентифицирует пользователя.
    """
    if user.username not in USERS_DB or USERS_DB[user.username]["master_password"] != user.master_password:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return {"message": "Login successful"}
