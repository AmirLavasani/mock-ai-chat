# AI Chat Application with FastAPI

This project aims to create a mock AI-powered chat application with a RESTful API using FastAPI. 

The application allows users to engage in mock AI-powered interactions, encapsulating multiple messages from both humans and AI.

## Objective

The primary objective is to create a chat application with the following API endpoints:

- Create a new interaction.
- Fetch all interactions.
- Create a message on an interaction.
- Fetch all messages in an interaction.

![the image of the openAPI docs endpoints](https://github.com/AmirLavasani/mock-ai-chat/blob/main/assets/images/mock-ai-chat-api-docs.png?raw=true)


## Table of Contents

1. [Installation](#installation)
2. [Project Structure](#project-structure)
3. [Endpoints](#endpoints)


### Prerequisites

- Conda installed - [Conda Installation Guide](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

## Installation

### Using docker-compose:

Run the following docker-compose command:

```bash
docker-compose up
```

To build the docker image:

```bash
docker-compose build
```

### Using the source:

1. Clone the repository:

    ```bash
    git clone git@github.com:AmirLavasani/mock-ai-chat.git
    ```

2. Navigate to the project directory:

    ```bash
    cd mock-ai-chat
    ```

3. Create a Conda environment:

    ```bash
    conda create --name chat-server python=3.11
    ```

4. Activate the Conda environment:

    ```bash
    conda activate chat-server
    ```

5. Install dependencies:

    ```bash
    make install-dev-deps
    make install-deps
    ```
6. Run the server:
    ```bash
    make run
    ```

> If you encountered missing imports run the following command:
export PYTHONPATH=\`pwd\` 

## Project Structure

### Directory Organization

#### Root Directory
- **README.md:** Describes project overview, setup instructions, and usage details.
- **.gitignore:** Specifies files and directories to ignore in version control.
- **requirements.txt:** Contains project dependencies for package installation.
- **docs:** Stores documentation files related to code and usage instructions.

#### App Directory
- **main.py:** Serves as the entry point, initializes the FastAPI application.
- **routers:** Houses API routers for different functionalities (e.g., `interactions_router.py`, `messages_router.py`).
- **schemas:** Contains Python classes defining interactions and messages (e.g., `interaction.py`, `message.py`).
- **utils:** Stores utility functions or helper methods used across the application.

### Main Files

#### main.py
- Initializes the FastAPI application.
- Imports routers and configures them within the application.

### Routers
- Utilizes FastAPI's `APIRouter()` to logically organize API endpoints.
- Registers routes, methods, and corresponding functions/handlers for each endpoint.

### Schemas
- Defines data models as Python classes using Pydantic models or plain classes.
- Includes methods for CRUD operations or data manipulation within these models.

### Documentation
- **docs:** Stores code documentation and usage guidelines.
- **README.md:** Describes project structure, setup instructions, and basic usage.
- Embeds docstrings and comments within the code to explain complex functionalities, particularly in models and routers.

- open docs/app/index.html to see the static documentation of the project.

![the image of the openAPI docs endpoints](https://github.com/AmirLavasani/mock-ai-chat/blob/main/assets/images/docs-screenshot.png?raw=true)

### Testing
- Uses `pytest app` to test the entire app.
- **tests:** Contains test files (e.g., `test_interaction.py`, `test_message.py`).
- Writes unit tests using frameworks like pytest to validate model, router, and utility functionality.

### Code Formatting and Linting
- Utilizes `make lint` for code formatting and linting throughout the app.
- Enforces consistent code style using tools like `black` for formatting and `flake8` for linting.
- Configures IDE or editor settings to comply with coding standards

## Endpoints

### Interactions
1. Create a new interaction
    - **POST** `/interactions`
    - Create a new interaction with provided settings.

2. Fetch all interactions
    - **GET** `/interactions`
    - Retrieve a list of all interactions.

3. Fetch one interaction by ID
    - **GET** `/interactions/{interaction_id}`
    - Retrieve a specific interaction by its ID.

### Messages
1. Create a new message
    - **POST** `/messages/{interaction_id}`
    - Create a new messages.

2. Fetch all messages
    - **GET** `/messages/{interaction_id}`
    - Retrieve a list of all messages in an interaction.

### Sample Output

A sample output of fetching all interaction objects with messages is provided.

### Fetch All Interaction Objects:

```json
{
  "data": [
    {
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
  ]
}
```

