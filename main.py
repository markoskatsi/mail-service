from fastapi import FastAPI
import os
from dotenv import load_dotenv
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import BaseModel, EmailStr, field_validator

load_dotenv()

conf = ConnectionConfig(
    MAIL_USERNAME="markoskatsi05@gmail.com",
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM="markoskatsi05@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_FROM_NAME="Markos Katsi",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=False,
)

app = FastAPI()


class EmailRequest(BaseModel):
    email: EmailStr
    name: str
    message: str

    @field_validator("name")
    def validate_name(cls, name):
        if not name.strip():
            raise ValueError("Please provide a name")
        if len(name) < 2:
            raise ValueError("Name must be at least 2 characters long")
        return name.strip()
    
    @field_validator("message")
    def validate_message(cls, message):
        if not message.strip():
            raise ValueError("Please provide a message")
        if len(message) < 4:
            raise ValueError("Please provide a more meaningful message")
        return message.strip()



@app.post("/email")
async def send_email(request: EmailRequest) -> JSONResponse:
    auto_reply = f"""<div style="font-family: system-ui, sans-serif, Arial; font-size: 16px;">
                        <p>Hi {request.name},</p>
                        <p>Thank you for reaching out! I've received your message, and will get back to you as soon as I can.</p>
                        <p>Best regards,<br>Markos Katsi</p>
                    </div>"""

    messages = [
        MessageSchema(
            subject="Message Received",
            recipients=[request.email],
            body=auto_reply,
            subtype=MessageType.html,
        ),
        MessageSchema(
            subject="New Message Received",
            recipients=["markoskatsi05@gmail.com"],
            body=f"<p>{request.name}, {request.email}</p><p>{request.message}</p>",
            subtype=MessageType.html,
        ),
    ]

    fm = FastMail(conf)
    await fm.send_message(messages)
    return JSONResponse(
        status_code=200, content={"status": 200, "message": "email has been sent"}
    )
