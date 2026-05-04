from pydantic import BaseModel, EmailStr, field_validator

class EmailRequest(BaseModel):
    email: EmailStr
    name: str
    message: str

    @field_validator("name")
    def validate_name(cls, name):
        name = name.strip()
        if not name:
            raise ValueError("Please provide a name")
        if len(name) < 2:
            raise ValueError("Name must be at least 2 characters long")
        return name

    @field_validator("message")
    def validate_message(cls, message):
        message = message.strip()
        if not message:
            raise ValueError("Please provide a message")
        if len(message) < 4:
            raise ValueError("Please provide a more meaningful message")
        return message
