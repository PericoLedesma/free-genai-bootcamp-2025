from fastapi import APIRouter, HTTPException

# from services.chat_claude import *
from services.get_transcript import get_transcript
from models import TranscriptRequest

DEFAULT_URL= "https://www.youtube.com/watch?v=gDg7rMJ9Odg&list=PLTF2DjpEk9qFI3npo8cw0cOk5dKGyaxNu"

transcript_router = APIRouter()


# ------------------ OPENAI CHAT ------------------ #
@transcript_router.post("/transcript/")
async def transcript(request: TranscriptRequest):
    print("\n\n===> ENDPOINT HIT: /transcript/")
    try:
        if not request.url:
            return {"transcript": get_transcript(DEFAULT_URL)}
            # raise HTTPException(status_code=400, detail="Missing url in the JSON body.")
        else:
            return {"transcript": get_transcript(request.url)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

''' Chat endpoint:
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=PNTCM7cbrsc"}' \
  http://127.0.0.1:8080/transcript/
'''
