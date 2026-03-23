from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.gemini_utils import answer_q

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post("/chat")
def chat(data: ChatRequest):
    reply = answer_q(data.query)
    return {"response": reply}
