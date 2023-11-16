from app.schemas.interaction import InteractionSetting, Interaction
from datetime import datetime
from uuid import uuid4, UUID
from typing import List

INTERACTIONS = []
INTERACTIONS_HASH = {}


async def create_interaction_crud(interaction_setting: InteractionSetting) -> UUID:
    """
    Create a new interaction with the provided settings.

    Args:
        interaction_setting (InteractionSetting): Settings for the new interaction.

    Returns:
        UUID: ID of the created interaction.
    """
    current_time = datetime.now()
    interaction_id = uuid4()

    new_interaction_data = {
        "id": interaction_id,
        "created_at": current_time,
        "updated_at": current_time,
        "settings": interaction_setting.dict(),
        "messages": [],
    }

    interaction = Interaction(**new_interaction_data)
    INTERACTIONS.append(interaction)
    INTERACTIONS_HASH[str(interaction_id)] = interaction

    return interaction_id


async def fetch_all_interactions_crud() -> List:
    """
    Retrieve all interactions.

    Returns:
        list: List of all interactions.
    """
    return INTERACTIONS


async def fetch_interaction_by_id_crud(interaction_id: str):
    """
    Retrieve a specific interaction by its ID.

    Args:
        interaction_id (str): ID of the interaction to retrieve.

    Returns:
        Interaction: The requested interaction.
    """
    return INTERACTIONS_HASH.get(interaction_id, None)
