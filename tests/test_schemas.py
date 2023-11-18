import pytest
from pydantic import ValidationError
from app.schemas.interaction import Interaction
from app.schemas.message import Message

def test_interaction_model():
    interaction_data = {
        "id": "ed227192-6f7e-4416-920c-6bc54400f194",
        "created_at": "2023-10-13T14:27:28",
        "updated_at": "2023-10-13T14:27:28",
        "settings": {
            "ai_model_name": "GPT4",
            "role": "System",
            "prompt": "As a helpful IFS therapist chatbot, your role is to guide users through a simulated IFS session in a safe and supportive manner with a few changes to the exact steps of the IFS model."
        },
        "messages": [
            {
                "id": "b190dac3-3bbd-4ac2-b87a-19fbb9693373",
                "created_at": "2023-10-13T14:27:37",
                "role": "human",
                "content": "Hello"
            },
            {
                "id": "fc8fdbd7-6721-41ad-86fe-9ee889c2f480",
                "created_at": "2023-10-13T14:27:39",
                "role": "ai",
                "content": "Hello! I'm here to guide you through a general daily check-in. Let's start by taking a few moments to find stillness. You might find it helpful to focus on your breath. Just take a few deep breaths in and out, and let's see what comes up for you."
            }
        ]
    }

    # Test valid interaction data
    interaction_model = Interaction(**interaction_data)
    assert str(interaction_model.id) == "ed227192-6f7e-4416-920c-6bc54400f194"
    assert len(interaction_model.messages) == 2

    # Test invalid interaction data
    with pytest.raises(ValidationError):
        # Change 'id' to an invalid type (int instead of str)
        interaction_data['id'] = 123
        Interaction(**interaction_data)

def test_message_model():
    message_data = {
        "id": "b190dac3-3bbd-4ac2-b87a-19fbb9693373",
        "created_at": "2023-10-13T14:27:37",
        "role": "human",
        "content": "Hello"
    }

    # Test valid message data
    message_model = Message(**message_data)
    assert message_model.role == "human"
    assert message_model.content == "Hello"

    # Test invalid message data
    with pytest.raises(ValidationError):
        # Remove the 'role' field
        del message_data['role']
        Message(**message_data)