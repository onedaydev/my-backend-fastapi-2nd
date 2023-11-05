from fastapi import APIRouter, BackgroundTasks


router = APIRouter(
    tags = ["backgroundtasks"],
)

def write_notification(email: str, message=""):
    with open("logs/backgroundtasks/log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

@router.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message='test message')
    return {"message" : "Notification sent in the background"}



