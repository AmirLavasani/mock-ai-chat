from typing import List
from pydantic import BaseModel
from fastapi import HTTPException, status

class InteractionCreateErrorResponse(BaseModel):
    type: str = "interaction.create_error"
    msg: str = "Interaction creation failed"
    loc: List[str] = ["controllers", "interaction"]

HTTPInteractionCreateErrorResponse = HTTPException(
    status_code=404, detail=InteractionCreateErrorResponse.model_dump()
)