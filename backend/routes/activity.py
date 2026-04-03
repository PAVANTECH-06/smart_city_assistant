from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.activity import UserActivity
from models.schemas import ActivityCreate

router = APIRouter(prefix="/activity", tags=["Activity"])

@router.post("/track")
def track_activity(data: ActivityCreate, db: Session = Depends(get_db)):
    activity = UserActivity(
        user_id=data.user_id,
        module_name=data.module_name
    )

    db.add(activity)
    db.commit()

    return {"message": "Activity tracked successfully"}