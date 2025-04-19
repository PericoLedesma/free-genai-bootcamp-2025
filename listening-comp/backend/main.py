import uvicorn
from fastapi import FastAPI
from api.chat_endpoint import chat_router
from api.get_transcript_endpoint import transcript_router
from api.structured_data_endpoint import struct_router
from db.rag import VectorDB

# Parameters
HOST = "127.0.0.1"
PORT = 8080

# Create the FastAPI app
app = FastAPI(title="German Learning Assistant API")
app.include_router(chat_router)
app.include_router(transcript_router)
app.include_router(struct_router)

# todo Include each router with a specific prefix and tag
# app.include_router(chat.router, prefix="/chat", tags=["Chat"])

# Root endpoint for testing:  http://127.0.0.1:8080
@app.get("/")
async def read_root():
    return {"message": "Welcome to the German Learning Assistant API"}

'''
@app.on_event("startup")  # This event is triggered when the server starts
async def startup_event():
    print("\t - Starting AWSBedrock client...")
    app.state.openai_client = ChatOpenAI() # Maybe one day 
    print("\t - Starting vector database...")
    app.state.vector_db = VectorDB(persist_directory="db/chroma_db")

'''

if __name__ == '__main__':
    print(f"\n****** Running the server at http://{HOST}:{PORT} ******\n")
    uvicorn.run("main:app",
                host=HOST,
                port=PORT,
                reload=True)

