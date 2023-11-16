from fastapi import APIRouter
from app.errors.error import HTTPInteractionCreateErrorResponse
from app.schemas.interaction import InteractionCreateSuccessResponse, InteractionSetting
from app.schemas import Interaction
from uuid import UUID, uuid4
from datetime import datetime

router = APIRouter()

@router.post("", response_model=InteractionCreateSuccessResponse, status_code=201)
async def create_interaction(interaction_setting: InteractionSetting):
    # Create the interaction
    current_time = datetime.now()

    # Example data for interaction creation (replace this with your actual data)
    new_interaction_data = {
        "id": uuid4(),  # Generating a new UUID for the interaction
        "created_at": current_time,
        "updated_at": current_time,
        "settings": interaction_setting,
        "messages": []
    }

    # Create the interaction using the CRUD function
    # created_interaction_id = create_interaction(Interaction(**new_interaction_data))
    return {"message": "New interaction created"}

@router.get("")
async def get_all_interactions():
    # Logic to fetch all interactions
    return {"message": "Get all interactions"}

@router.get("/{interaction_id}")
async def get_one_interaction():
    # Logic to fetch one interaction by interaction_id
    return {"message": "Get one interaction with interaction_id"}