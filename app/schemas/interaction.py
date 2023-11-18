from typing import List
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
    ai_model_name: str = "GPT-3"
    role: str = "System"
    prompt: str = "Sample prompt for testing"
