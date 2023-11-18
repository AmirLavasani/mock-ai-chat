from fastapi import APIRouter
from typing import List
from app.schemas.message import Message, MessageCreateSuccessResponse
from app.errors.error import (
    HTTPMessageCreateErrorResponse,
    HTTPMessageFetchErrorResponse,
)
from app.crud.db import create_message_crud, fetch_all_messages_crud

router = APIRouter()


@router.post("/{interaction_id}")
async def create_message(interaction_id: str, content: str, role: str):
    """
    Create a new message for a specific interaction.

    Args:
        interaction_id (str): The ID of the interaction.
        content (str): The content of the message.
        role (str): The role of the message (e.g., 'human' or 'ai').

    Returns:
        MessageCreateSuccessResponse: Response containing the created message ID.
    """

    created_message_id = await create_message_crud(interaction_id, content, role)
    if not created_message_id:
        raise HTTPMessageCreateErrorResponse
    return MessageCreateSuccessResponse(id=str(created_message_id))


@router.get("/{interaction_id}", response_model=List[Message])
async def get_all_messages(interaction_id: str):
    """
    Retrieve all messages for a specific interaction.

    Args:
        interaction_id (str): The ID of the interaction.

    Returns:
        List[Message]: List of all messages for the interaction.
    """

    messages = await fetch_all_messages_crud(interaction_id)
    if messages is None:
        raise HTTPMessageFetchErrorResponse
    return messages
