from fastapi import APIRouter
from pydantic import BaseModel
from services.gemini_utils import summarize_text

router = APIRouter()

class SummarizeRequest(BaseModel):
    text: str

@router.post("/summarize")
def summarize(data: SummarizeRequest):
    result = summarize_text(data.text)
    return {"summary": result}
