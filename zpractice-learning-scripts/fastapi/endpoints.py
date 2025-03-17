from fastapi import APIRouter
from services import get_greeting
from services import test2
from pydantic import BaseModel

router = APIRouter()

 #  ----------------- POST Request ----------------- #
class Item(BaseModel):
    name: str
    description: str

'''
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"name": "Example Item", "description": "This is an example description"}' \
  http://127.0.0.1:8080/items/

'''
@router.post("/items/")
async def create_item(item: Item):
    return {"item": item}

 #  ----------------- GET Request ----------------- #
# http://127.0.0.1:8080/greet?name=John&age=30&country=Canada
@router.get("/greet")
async def greet(name: str = "World",
                age: int = 25,
                country: str = "USA"):
    return {"message": f"Hello, {name}! You are {age} years old from {country}."}

# http://127.0.0.1:8080/greet3/John/30/Canada
@router.get("/greet3/{name}/{age}/{country}")
async def greet(name: str = "World",
                age: int = 25,
                country: str = "USA"):
    return {"message": f"Hello, {name}! You are {age} years old from {country}."}


''' Frontend Request (JSON format):

fetch("http://localhost:8000/greet", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name: "John", age: 30, country: "Canada" })
})
.then(response => response.json())
.then(data => console.log(data));
'''

@router.get("/test")
async def test():
    """
    Returns a greeting message.
    - **name**: The name to include in the greeting (default is "World").
    """
    return {"message": test2()}

@router.get("/help")
async def help():
    """
    Returns a greeting message.
    - **name**: The name to include in the greeting (default is "World").
    """
    return {"message": "Help yourself"}
