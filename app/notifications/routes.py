from fastapi import APIRouter
from app.notifications.models import Notification

router = APIRouter()

@router.post("/notify/")
async def notify(notification: Notification):
    return {"message": "Notification sent"}

@router.get("/history/{user_id}")
async def get_notification_history(user_id: int):
    return {"user_id": user_id, "notifications": []}
