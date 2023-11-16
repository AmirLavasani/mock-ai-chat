from pydantic import BaseModel


class Message(BaseModel):
    id: str
    created_at: str
    role: str
    content: str