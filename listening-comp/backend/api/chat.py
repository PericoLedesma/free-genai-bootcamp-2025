from fastapi import FastAPI, HTTPException
from fastapi import APIRouter
from models import *
from services.chat_claude import *

from flask import Flask, request, jsonify


router = APIRouter()

# Chat with Claude endpoint
@router.post("/chat")
async def chat_with_claude(request: ChatRequest):

    return {"response": reply}

    try:
        req_data = request.get_json()
        if not req_data or "prompt" not in req_data:
            return jsonify({"error": "Missing prompt parameter in the JSON body."}), 400

        prompt = req_data["prompt"]
        result = chat_with_claude(prompt)


        reply = f"Claude received: {request.message}"
        return {"response": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




# # Chat with Claude endpoint
# @router.post("/chat")
# async def chat_with_claude(request: ChatRequest):
#     try:
#         # Here you would normally call your LLM client.
#         # For demonstration, we'll just echo the message.
#         reply = f"Claude received: {request.message}"
#         return {"response": reply}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
