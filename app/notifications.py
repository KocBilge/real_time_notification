from app.celery_worker import send_async_notification

def send_notification(notification):
    user_id = notification.user_id
    message = notification.message

    send_async_notification.delay(user_id, message)
