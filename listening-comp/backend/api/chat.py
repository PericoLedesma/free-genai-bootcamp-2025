from fastapi import APIRouter, HTTPException
from services.chat_AWS import AWSBedrockClient

# from services.chat_claude import *
from services.chat_openai import chat_openai
from models import ChatRequest

chat_router = APIRouter()

''' Chat endpoint:
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-4o", "prompt": "Hello chatgpt, are you there?"}' \
  http://127.0.0.1:8080/chatopenai/

'''

@chat_router.post("/chatopenai/")
async def chat_with_openai(request: ChatRequest):
    try:
        # Directly access the prompt attribute from the Pydantic model.
        if not request.prompt:
            raise HTTPException(status_code=400, detail="Missing prompt parameter in the JSON body.")

        prompt = request.prompt
        # return {"response": "Prompt: " + prompt}
        return {"response": chat_openai(request.prompt, request.model)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# New endpoint to talk to AWS Bedrock service
bedrock_client = AWSBedrockClient()


'''
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Describe the purpose of a hello world program."}' \
  http://127.0.0.1:8080/chatbedrock/
'''
@chat_router.post("/chatbedrock/")
async def chat_with_bedrock(request: ChatRequest):
    try:
        if not request.prompt:
            raise HTTPException(status_code=400, detail="Missing prompt parameter in the JSON body.")
        # Invoke the Bedrock service synchronously
        response = bedrock_client.invoke_model(request.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
