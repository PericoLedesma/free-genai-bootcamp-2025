from pydantic import BaseModel

# By inheriting from BaseModel, ChatRequest becomes a data model that automatically validates and parses input data.

# Define data models for incoming requests
class ChatRequest(BaseModel):
    model: str = "ChatGPT"  # Default value if not provided
    message: str

class GrammarRequest(BaseModel):
    sentence: str

class AlignmentRequest(BaseModel):
    scenario: str

class ReasoningRequest(BaseModel):
    problem: str
