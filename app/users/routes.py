from fastapi import APIRouter
from app.users.models import UserCreate

router = APIRouter()

@router.post("/register/")
async def register_user(user: UserCreate):
    return {"message": "User registered"}

@router.get("/profile/{user_id}")
async def get_user_profile(user_id: int):
    return {"user_id": user_id}
