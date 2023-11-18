from typing import List
from pydantic import BaseModel
from fastapi import HTTPException


class InteractionCreateErrorResponse(BaseModel):
    type: str = "interaction.create_error"
    msg: str = "Interaction creation failed"
    loc: List[str] = ["controllers", "interaction"]


HTTPInteractionCreateErrorResponse = HTTPException(
    status_code=404, detail=InteractionCreateErrorResponse().model_dump()
)


class InteractionFetchErrorResponse(BaseModel):
    type: str = "interaction.fetch_error"
    msg: str = "Interaction fetch failed"
    loc: List[str] = ["controllers", "interaction"]


HTTPInteractionFetchErrorResponse = HTTPException(
    status_code=404, detail=InteractionFetchErrorResponse().model_dump()
)


class MessageCreateErrorResponse(BaseModel):
    type: str = "message.create_error"
    msg: str = "Message creation failed"
    loc: List[str] = ["controllers", "message"]


HTTPMessageCreateErrorResponse = HTTPException(
    status_code=404, detail=MessageCreateErrorResponse().model_dump()
)


class MessageFetchErrorResponse(BaseModel):
    type: str = "message.fetch_error"
    msg: str = "Message fetch failed"
    loc: List[str] = ["controllers", "message"]


HTTPMessageFetchErrorResponse = HTTPException(
    status_code=404, detail=MessageFetchErrorResponse().model_dump()
)
