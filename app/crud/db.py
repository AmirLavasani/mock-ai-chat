from app.schemas.interaction import InteractionSetting, Interaction
from app.schemas.message import Message
from datetime import datetime
from uuid import uuid4, UUID
from typing import List, Optional

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
        "settings": interaction_setting.model_dump(),
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


async def fetch_interaction_by_id_crud(interaction_id: str) -> Optional[Interaction]:
    """
    Retrieve a specific interaction by its ID.

    Args:
        interaction_id (str): ID of the interaction to retrieve.

    Returns:
        Interaction: The requested interaction.
    """
    return INTERACTIONS_HASH.get(interaction_id, None)


async def create_message_crud(interaction_id: str, content: str, role: str) -> Optional[UUID]:
    
    """
    Create a new message for a specific interaction.

    Args:
        interaction_id (str): The ID of the interaction.
        content (str): The content of the message.
        role (str): The role of the message (e.g., 'human' or 'ai').

    Returns:
        Optional[UUID]: The ID of the created message, if successful, else None.
    """
    interaction = INTERACTIONS_HASH.get(interaction_id, None)

    # interaction does not exist
    if interaction is None:
        return None

    current_time = datetime.now()
    message_id = uuid4()

    new_message_data = {
        "id": message_id,
        "created_at": current_time,
        "role": role,
        "content": content,
    }

    message = Message(**new_message_data)
    interaction.messages.append(message)

    return message_id


async def fetch_all_messages_crud(interaction_id: str) -> Optional[List[Message]]:
    """
    Retrieve all messages for a specific interaction.

    Args:
        interaction_id (str): The ID of the interaction.

    Returns:
        Optional[List[Message]]: List of all messages for the interaction, if found, else None.
    """
    interaction = INTERACTIONS_HASH.get(interaction_id, None)

    # interaction does not exist
    if interaction is None:
        return None

    return interaction.messages
