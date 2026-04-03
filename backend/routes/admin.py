from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import get_db
from models.user import User
from models.activity import UserActivity
from models.feedback import Feedback

router = APIRouter(prefix="/admin", tags=["Admin"])

# -----------------------------
# TOTAL USERS
# -----------------------------
@router.get("/total-users")
def total_users(db: Session = Depends(get_db)):
    return {"total_users": db.query(User).count()}

# -----------------------------
# MODULE USAGE
# -----------------------------
@router.get("/module-usage")
def module_usage(db: Session = Depends(get_db)):
    usage = db.query(
        UserActivity.module_name,
        func.count(UserActivity.id)
    ).group_by(UserActivity.module_name).all()

    return [{"module": u[0], "count": u[1]} for u in usage]

# -----------------------------
# FEEDBACK LIST
# -----------------------------
@router.get("/feedbacks")
def get_feedbacks(db: Session = Depends(get_db)):
    feedbacks = db.query(Feedback).all()

    return [
        {
            "user_id": f.user_id,
            "message": f.message,
            "timestamp": f.timestamp
        }
        for f in feedbacks
    ]

# -----------------------------
# ACTIVE USERS (NEW 🔥)
# -----------------------------
@router.get("/active-users")
def active_users(db: Session = Depends(get_db)):
    active = db.query(
        UserActivity.user_id,
        func.count(UserActivity.id)
    ).group_by(UserActivity.user_id).all()

    return [{"user_id": a[0], "activity_count": a[1]} for a in active]