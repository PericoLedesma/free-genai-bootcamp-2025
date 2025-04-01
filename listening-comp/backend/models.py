from pydantic import BaseModel

# By inheriting from BaseModel, ChatRequest becomes a data model that automatically validates and parses input data.

# Define data models for incoming requests
class ChatRequest(BaseModel):
    model: str = "gpt-4o"  # Default value if not provided
    prompt: str

class TranscriptRequest(BaseModel):
    url: str

class StructDataRequest(BaseModel):
    video_id: str

class ReasoningRequest(BaseModel):
    problem: str
