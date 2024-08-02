from pydantic import BaseModel
from typing import Optional

class Notification(BaseModel):
    user_id: int
    message: str
    category: Optional[str] = "general"  # Bildirim kategorisi

class NotificationHistory(BaseModel):
    user_id: int
    notifications: list[Notification]
