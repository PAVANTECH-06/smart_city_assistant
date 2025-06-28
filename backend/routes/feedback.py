from fastapi import APIRouter
from models.schemas import Feedback

router = APIRouter()
feedback_db = []

@router.post("/feedback")
def submit_feedback(data: Feedback):
    feedback_db.append(data.dict())
    return {"message": "Feedback submitted"}