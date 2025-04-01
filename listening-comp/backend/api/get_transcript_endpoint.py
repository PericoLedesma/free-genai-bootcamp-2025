from fastapi import APIRouter, HTTPException
from services.get_transcript import extract_transcript
from models import TranscriptRequest

DEFAULT_URL = "https://www.youtube.com/watch?v=hhuNW1COrSM"

transcript_router = APIRouter()

@transcript_router.post("/transcript/")
async def transcript(request: TranscriptRequest):
    print("\n\n===> ENDPOINT HIT: /transcript/")
    try:
        if not request.url:
            print("Ojo: No URL provided. Using default URL.")
            video_title, video_id, transcript = extract_transcript(DEFAULT_URL)
            # raise HTTPException(status_code=400, detail="Missing url in the JSON body.")
        else:
            video_title, video_id, transcript = extract_transcript(request.url)

        return {"video_title": video_title,
                "video_id": video_id,
                "transcript": transcript}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


''' Chat endpoint:
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=PNTCM7cbrsc"}' \
  http://127.0.0.1:8080/transcript/
'''
