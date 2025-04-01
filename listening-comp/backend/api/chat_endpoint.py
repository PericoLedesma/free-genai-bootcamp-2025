from fastapi import APIRouter, HTTPException
from models import ChatRequest

# from services.chat_claude import *
from services.chat_AWS import AWSBedrockClient
from services.chat_openai import ChatOpenAI

chat_router = APIRouter()
openai_client = ChatOpenAI()
bedrock_client = AWSBedrockClient()


# ------------------ OPENAI CHAT ------------------ #
@chat_router.post("/chatopenai/")
async def chat_with_openai(request: ChatRequest):
    print("\n\n===>ENDPOINT HIT: /chatopenai/")
    try:
        # Directly access the prompt attribute from the Pydantic model.
        if not request.prompt:
            raise HTTPException(status_code=400, detail="Missing prompt parameter in the JSON body.")
        prompt = request.prompt
        # return {"response": "Prompt: " + prompt}
        return {"response": openai_client.chat(request.prompt, request.model)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

''' Chat endpoint:
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-4o", "prompt": "Hello chatgpt, are you there?"}' \
  http://127.0.0.1:8080/chatopenai/
'''

# ------------------ BEDROCK CHAT ------------------ #
@chat_router.post("/chatbedrock/")
async def chat_with_bedrock(request: ChatRequest):
    print("\n\n===>ENDPOINT HIT: /chatbedrock/")
    try:
        if not request.prompt:
            raise HTTPException(status_code=400, detail="Missing prompt parameter in the JSON body.")
        # Invoke the Bedrock service synchronously
        response = bedrock_client.invoke_model(request.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

'''
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Describe the purpose of a hello world program."}' \
  http://127.0.0.1:8080/chatbedrock/
'''