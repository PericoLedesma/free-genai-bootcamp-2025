import uvicorn
from fastapi import FastAPI
from api.chat_endpoint import chat_router
from api.get_transcript_endpoint import transcript_router
# from app.api.endpoints import chat, grammar, alignment, reasoning

# Parameters
HOST = "127.0.0.1"
PORT = 8080

# Create the FastAPI app
app = FastAPI(title="German Learning Assistant API")
app.include_router(chat_router)
app.include_router(transcript_router)

# # Include each router with a specific prefix and tag
# app.include_router(chat.router, prefix="/chat", tags=["Chat"])
# app.include_router(grammar.router, prefix="/grammar", tags=["Grammar"])
# app.include_router(alignment.router, prefix="/alignment", tags=["Alignment"])
# app.include_router(reasoning.router, prefix="/reasoning", tags=["Reasoning"])

# Root endpoint for testing:  http://127.0.0.1:8080
@app.get("/")
async def read_root():
    return {"message": "Welcome to the German Learning Assistant API"}

@app.on_event("startup") # This event is triggered when the server starts
async def startup_event():
    app.state.my_client = "AWSBedrockClient() "


if __name__ == '__main__':
    print("Running the server at http://")
    uvicorn.run("main:app",
                host=HOST,
                port=PORT,
                reload=True)






# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
#
# app = FastAPI(title="German Learning Assistant API")
#
#
# # Root endpoint to verify that the server is running
# @app.get("/")
# async def read_root():
#     return {"message": "Welcome to the German Learning Assistant API"}
#
#
# # Grammar analysis endpoint
# @app.post("/grammar")
# async def analyze_grammar(request: GrammarRequest):
#     try:
#         # Dummy grammar analysis response
#         analysis = f"Analyzing grammar for: {request.sentence}"
#         return {"analysis": analysis}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#
# # Agent-Based Alignment Generation endpoint
# @app.post("/alignment")
# async def generate_alignment(request: AlignmentRequest):
#     try:
#         # Dummy alignment response
#         alignment = f"Generated alignment for scenario: {request.scenario}"
#         return {"alignment": alignment}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#
# # Agent-Based Reasoning endpoint
# @app.post("/reasoning")
# async def run_reasoning(request: ReasoningRequest):
#     try:
#         # Dummy reasoning response
#         result = f"Reasoning result for problem: {request.problem}"
#         return {"result": result}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
