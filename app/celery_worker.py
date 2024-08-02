from celery import Celery

celery_app = Celery(
    'notification_tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

@celery_app.task
def send_async_notification(user_id, message):
    print(f"Sending notification to user {user_id}: {message}")
