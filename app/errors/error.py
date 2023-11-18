from typing import List
from pydantic import BaseModel
from fastapi import HTTPException


class InteractionCreateErrorResponse(BaseModel):
    type: str = "interaction.create_error"
    msg: str = "Interaction creation failed"
    loc: List[str] = ["controllers", "interaction"]


HTTPInteractionCreateErrorResponse = HTTPException(
    status_code=404, detail=InteractionCreateErrorResponse().dict()
)


class InteractionFetchErrorResponse(BaseModel):
    type: str = "interaction.fetch_error"
    msg: str = "Interaction fetch failed"
    loc: List[str] = ["controllers", "interaction"]


HTTPInteractionFetchErrorResponse = HTTPException(
    status_code=404, detail=InteractionFetchErrorResponse().dict()
)


class MessageCreateErrorResponse(BaseModel):
    type: str = "message.create_error"
    msg: str = "Message creation failed"
    loc: List[str] = ["controllers", "message"]


HTTPMessageCreateErrorResponse = HTTPException(
    status_code=404, detail=MessageCreateErrorResponse().dict()
)


class MessageFetchErrorResponse(BaseModel):
    type: str = "message.fetch_error"
    msg: str = "Message fetch failed"
    loc: List[str] = ["controllers", "message"]


HTTPMessageFetchErrorResponse = HTTPException(
    status_code=404, detail=MessageFetchErrorResponse().dict()
)
