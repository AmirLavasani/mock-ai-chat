from typing import List, Optional
from pydantic import BaseModel, UUID4
from .message import Message
from datetime import datetime


class Interaction(BaseModel):
    id: UUID4
    created_at: datetime
    updated_at: datetime
    settings: dict
    messages: List[Message]


class InteractionCreateSuccessResponse(BaseModel):
    id: UUID4


class InteractionSetting(BaseModel):
    model_name: str
    role: str
    prompt: str
