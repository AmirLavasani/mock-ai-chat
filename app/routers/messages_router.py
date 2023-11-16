from fastapi import APIRouter
from typing import List
from app.schemas.message import Message  # Import the Message Pydantic model

router = APIRouter()


# Updated route to receive a Message model and return an empty 200 response
@router.post("/{interaction_id}")
async def create_message(message: Message):
    # Logic to create a message in a specific interaction
    # You can use the 'message' data received to process/store the message
    return {}


# Updated route to receive an interaction ID and return a list of Messages
@router.get("/{interaction_id}", response_model=List[Message])
async def get_all_messages():
    # Logic to fetch all messages in a specific interaction
    # Replace this with the actual code to retrieve messages based on 'interaction_id'
    messages = []  # Placeholder for retrieved messages
    return messages
