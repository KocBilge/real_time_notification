from fastapi import FastAPI, BackgroundTasks, WebSocket, HTTPException
from pydantic import BaseModel
from app.notifications import send_notification
from app.core.exceptions import http_exception_handler

app = FastAPI()

app.add_exception_handler(HTTPException, http_exception_handler)

class Notification(BaseModel):
    user_id: int
    message: str

@app.post("/notify/")
async def notify(notification: Notification, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_notification, notification)
    return {"message": "Notification scheduled"}

@app.get("/")
async def read_root():
    return {"message": "Real-Time Notification System"}

@app.websocket("/ws/notifications/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Notification for user {user_id}: {data}")