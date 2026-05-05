from fastapi import APIRouter
from pydantic import EmailStr
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, MessageType
from config import conf
from schemas import EmailRequest

router = APIRouter()


@router.post("/contact")
async def send_contact_message(request: EmailRequest) -> JSONResponse:
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
    return JSONResponse(content={"message": "email has been sent"})


@router.post("/cv")
async def send_cv(email: EmailStr) -> JSONResponse:
    message = MessageSchema(
        subject="CV Request",
        recipients=[email],
        body="<p>Hi,</p><p>Please find attached my CV.</p><p>Best regards,<br>Markos Katsi</p>",
        subtype=MessageType.html,
        attachments=["./assets/MarkosKatsiCV.pdf"],
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(content={"message": "CV has been sent"})
