from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.feedback import Feedback
from models.schemas import FeedbackCreate

router = APIRouter(prefix="/feedback", tags=["Feedback"])

# -----------------------------
# ADD FEEDBACK (STORE IN DB)
# -----------------------------
@router.post("/")
def submit_feedback(data: FeedbackCreate, db: Session = Depends(get_db)):
    new_feedback = Feedback(
        user_id=data.user_id,
        message=data.message
    )

    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)

    return {"message": "Feedback submitted successfully"}