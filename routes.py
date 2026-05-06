from fastapi import APIRouter
from pydantic import EmailStr
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, MessageType
from config import conf
from schemas import EmailRequest
from email_templates import generate_auto_reply, generate_admin_notification, generate_cv_email

router = APIRouter()


@router.post("/contact")
async def send_contact_message(request: EmailRequest) -> JSONResponse:
    auto_reply = generate_auto_reply(request)
    admin_notification = generate_admin_notification(request)

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
            body=admin_notification,
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
        body=generate_cv_email(),
        subtype=MessageType.html,
        attachments=["./assets/MarkosKatsiCV.pdf"],
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(content={"message": "CV has been sent"})
