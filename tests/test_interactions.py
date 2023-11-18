import json
from typing import List
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Initialize interaction_id variable
interaction_id = None


# Test create_interaction endpoint
def test_create_interaction():
    global interaction_id  # Use the interaction_id variable from the outer scope

    # Create a sample InteractionSetting object
    sample_interaction_setting = {
        "ai_model_name": "GPT-3",
        "role": "System",
        "prompt": "Sample prompt for testing"
    }

    response = client.post("/interactions/", json=sample_interaction_setting)
    assert response.status_code == 201
    assert "id" in response.json()

    # Extract the interaction_id for subsequent tests
    interaction_id = response.json()["id"]

# Test get_all_interactions endpoint
def test_get_all_interactions():
    response = client.get("/interactions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test get_one_interaction endpoint
def test_get_one_interaction():
    global interaction_id  # Use the interaction_id variable from the outer scope

    # Check if an interaction ID is available
    assert interaction_id is not None, "No interaction ID available for testing"

    # Use the interaction ID obtained from the previous test
    response = client.get(f"/interactions/{interaction_id}")
    assert response.status_code == 200
    assert "id" in response.json()