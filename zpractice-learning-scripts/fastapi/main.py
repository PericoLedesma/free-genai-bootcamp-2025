from fastapi import FastAPI
from endpoints import router as api_router

app = FastAPI()
app.include_router(api_router)

# Root endpoint for testing
@app.get("/")
async def read_root():
    return {"message": "Root endpoint"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)



'''
Uvicorn is a lightning-fast ASGI (Asynchronous Server Gateway Interface) server implementation for Python. It’s designed to serve asynchronous web frameworks like FastAPI, Starlette, and others. 
Uvicorn acts as a bridge between your FastAPI   (or any ASGI-based) application and the internet, efficiently handling HTTP requests and responses.
'''