from pydantic import BaseModel, UUID4
from datetime import datetime


class Message(BaseModel):
    id: UUID4
    created_at: datetime
    role: str
    content: str


class MessageCreateSuccessResponse(BaseModel):
    id: UUID4
