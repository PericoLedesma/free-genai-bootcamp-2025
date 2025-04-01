# FastAPI Backend Overview

This FastAPI backend server is designed to serve as the backend for a German Learning Assistant API. 

It provides several endpoints to handle functionalities such as chatting with Claude, performing grammar analysis, generating agent-based alignment, and executing multi-step reasoning.

## Key Components

### 1. Entry Point (main.py)

The entry point sets up the FastAPI app, includes all the API routers, and provides a root endpoint to verify that the API is running.

#### Example Code:

```python
from fastapi import FastAPI
from app.api.endpoints import chat, grammar, alignment, reasoning

app = FastAPI(title="German Learning Assistant API")

# Include each router with a specific prefix and tag
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(grammar.router, prefix="/grammar", tags=["Grammar"])
app.include_router(alignment.router, prefix="/alignment", tags=["Alignment"])
app.include_router(reasoning.router, prefix="/reasoning", tags=["Reasoning"])

# Root endpoint for testing
@app.get("/")
async def read_root():
    return {"message": "Welcome to the German Learning Assistant API"}
```

### 2. API Endpoints

Each endpoint corresponds to a specific feature:

- **Chat with Claude (chat.py):** Receives a message from the client, processes it (e.g., via a language model), and returns a response.
- **Grammar Analysis (grammar.py):** Accepts a german sentence and returns a grammar analysis.
- **Agent-Based Alignment Generation (alignment.py):** Takes a scenario description and returns a generated alignment demonstration.
- **Agent-Based Reasoning (reasoning.py):** Processes a complex problem statement and returns reasoning or step-by-step results.

#### Example Endpoint Code (Chat):

```python
# backend/app/api/endpoints/chat_endpoint.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core import llm_client

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/")
async def chat_with_claude(request: ChatRequest):
    try:
        # Call the LLM client to process the message
        response = await llm_client.get_chat_response(request.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

### 3. Core Logic and LLM Client (xxx.py)

**Purpose:**
Encapsulates the logic for interacting with external language model APIs. This separation allows you to update the LLM integration without modifying endpoint code.

#### Example Code:

```python
# backend/app/core/llm_client.py
import httpx

async def get_chat_response(message: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.post("https://api.claude.ai/chat", json={"prompt": message})
        data = response.json()
    return data.get("reply", "No response")

async def analyze_grammar(sentence: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.post("https://api.example.com/grammar", json={"sentence": sentence})
        data = response.json()
    return data.get("analysis", "No analysis available")

async def generate_alignment(scenario: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.post("https://api.example.com/alignment", json={"scenario": scenario})
        data = response.json()
    return data.get("alignment", "No alignment available")

async def solve_problem(problem: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.post("https://api.example.com/reasoning", json={"problem": problem})
        data = response.json()
    return data.get("result", "No result available")
```

### 4. Configuration (config.py)

**Purpose:**
Handles configuration and environment variables, such as API keys and external service URLs, using libraries like `python-dotenv`.

#### Example Code:

```python
# backend/app/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

LLM_API_KEY = os.getenv("LLM_API_KEY", "your-default-key")
LLM_CHAT_URL = os.getenv("LLM_CHAT_URL", "https://api.claude.ai/chat")
# Add additional configuration variables as needed.
```

## How It Works

### FastAPI Setup
- The FastAPI instance is initialized and each functional area (chat, grammar, alignment, reasoning) is routed with its own endpoint. This ensures modularity and clarity.

### Request Validation
- Pydantic models (e.g., `ChatRequest`) are used for input validation, ensuring that endpoints receive correctly structured data.

### Error Handling
- Each endpoint uses `try-except` blocks to catch exceptions. In case of an error, an HTTP 500 status code is returned with a descriptive error message.

### Separation of Concerns
- The backend logic is separated into different modules:
  - **Endpoints:** Handle API routing and input/output.
  - **Core Module:** Contains the logic for interacting with external services.
  - **Configuration:** Manages environment-specific settings and API keys.

### Extensibility
- The backend structure is designed to be scalable. Adding new endpoints or features involves creating additional modules under the `endpoints` directory and integrating new functions in the `llm_client` or other core modules.

### Interactive Documentation
- When the server is running, FastAPI automatically generates interactive API documentation (Swagger UI) accessible at `/docs`, which is invaluable for testing and debugging.

## Running the Server
```sh
uvicorn app.main:app --reload
```

### Access the API:
- Visit [http://localhost:8000](http://localhost:8000) to check the root endpoint.
- Visit [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive API documentation.


### Uvicorn

Uvicorn is a lightning-fast ASGI (Asynchronous Server Gateway Interface) server implementation for Python. It’s designed to serve asynchronous web frameworks like FastAPI, Starlette, and others. 
Uvicorn acts as a bridge between your FastAPI (or any ASGI-based) application and the internet, efficiently handling HTTP requests and responses.