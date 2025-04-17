from fastapi import APIRouter, HTTPException
from services.structured_data import lets_structure_data
from models import StructDataRequest

struct_router = APIRouter()


@struct_router.post("/structdata/")
async def structdata(request: StructDataRequest):
    print("\n\n===> ENDPOINT HIT: /structdata/")
    try:
        if not request.id:
            raise HTTPException(status_code=400, detail="Missing model_id in the JSON body.")
        else:
            # return {"transcript": "hola"}
            transcript, struct_transcript = lets_structure_data(request.id)
            print("****** Completed receiveing answer of the llm ******")
            return {"transcript": transcript,
                    "struct_transcript": struct_transcript}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
