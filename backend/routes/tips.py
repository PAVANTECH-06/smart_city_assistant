from fastapi import APIRouter
from pydantic import BaseModel
from services.gemini_utils import gentip

router = APIRouter()

class TipRequest(BaseModel):
    keyword: str

@router.post("/tips")
def eco_tips(data: TipRequest):
    tip = gentip(data.keyword)
    return {"tips": tip}
