from fastapi import APIRouter, HTTPException
from services.get_transcript import lets_structure_data
from models import StructDataRequest


struct_router = APIRouter()


# ------------------ OPENAI CHAT ------------------ #
@struct_router.post("/structdata/")
async def structdata(request: StructDataRequest):
    print("\n\n===> ENDPOINT HIT: /structdata/")
    try:
        if not request.model_id:
            raise HTTPException(status_code=400, detail="Missing model_id in the JSON body.")
        else:

            # video_id, transcript = extract_transcript(request.url)
            # return {"transcript": transcript, "video_id": video_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

''' Chat endpoint:
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=PNTCM7cbrsc"}' \
  http://127.0.0.1:8080/transcript/
'''
