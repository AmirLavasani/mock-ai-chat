from typing import List

from fastapi import APIRouter, status

from app.errors.error import (
    HTTPInteractionCreateErrorResponse,
    HTTPInteractionFetchErrorResponse,
)
from app.schemas.interaction import (
    InteractionCreateSuccessResponse,
    InteractionSetting,
    Interaction,
)
from app.crud.db import (
    create_interaction_crud,
    fetch_all_interactions_crud,
    fetch_interaction_by_id_crud,
)


router = APIRouter()


@router.post(
    "/",
    response_model=InteractionCreateSuccessResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_interaction(interaction_setting: InteractionSetting):
    """
    Create a new interaction with the provided settings.

    Args:
        interaction_setting (InteractionSetting): Settings for the new interaction.

    Returns:
        InteractionCreateSuccessResponse: Response containing the created interaction ID.
    """
    created_interaction_id = await create_interaction_crud(interaction_setting)
    if not created_interaction_id:
        raise HTTPInteractionCreateErrorResponse
    return InteractionCreateSuccessResponse(id=str(created_interaction_id))


@router.get("/", response_model=List[Interaction], status_code=status.HTTP_200_OK)
async def get_all_interactions():
    """
    Retrieve all interactions.

    Returns:
        List[Interaction]: List of all interactions.
    """
    interactions = await fetch_all_interactions_crud()
    return interactions


@router.get(
    "/{interaction_id}", response_model=Interaction, status_code=status.HTTP_200_OK
)
async def get_one_interaction(interaction_id: str):
    """
    Retrieve a specific interaction by its ID.

    Args:
        interaction_id (str): ID of the interaction to retrieve.

    Returns:
        Interaction: The requested interaction.
    """
    interaction = await fetch_interaction_by_id_crud(interaction_id)
    if interaction is None:
        raise HTTPInteractionFetchErrorResponse
    return interaction
