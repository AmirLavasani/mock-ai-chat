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
