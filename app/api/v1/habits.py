from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db
from app.schemas.habit import HabitCreate, HabitResponse
from app.services.habit_service import HabitService

router = APIRouter(
    prefix="/habits",
    tags=["Habits"]
)


@router.post("/", response_model=HabitResponse)
def create_habit(
    habit_data: HabitCreate,
    db: Session = Depends(get_db)
):
    return HabitService.create_habit(db, habit_data)


@router.get("/", response_model=List[HabitResponse])
def get_habits(
    db: Session = Depends(get_db)
):
    return HabitService.get_all_habits(db)
