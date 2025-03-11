from fastapi import APIRouter
from services import get_greeting

router = APIRouter()

@router.get("/greet")
async def greet(name: str = "World!"):
    """
    Returns a greeting message.
    - **name**: The name to include in the greeting (default is "World").
    """
    return {"message": get_greeting(name)}
