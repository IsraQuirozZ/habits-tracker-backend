from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db
from app.schemas.habit import HabitCreate, HabitResponse, HabitUpdate
from app.services.habit_service import HabitService

router = APIRouter(
    prefix="/habits",
    tags=["Habits"]
)

@router.get("/", response_model=List[HabitResponse])
def get_habits(
    db: Session = Depends(get_db)
):
    return HabitService.get_all_habits(db)


@router.get("/{habit_id}", response_model=HabitResponse)
def get_habit(
    habit_id: int,
    db: Session = Depends(get_db)
):
    return HabitService.get_habit_by_id(db, habit_id)

@router.post("/", response_model=HabitResponse)
def create_habit(
    habit_data: HabitCreate,
    db: Session = Depends(get_db)
):
    return HabitService.create_habit(db, habit_data)


@router.put("/{habit_id}", response_model=HabitResponse)
def update_habit(
    habit_id: int,
    habit_data: HabitUpdate,
    db: Session = Depends(get_db)
):
    return HabitService.update_habit_by_id(db, habit_id, habit_data)

@router.delete("/{habit_id}", response_model=HabitResponse)
def delete_habit(
    habit_id: int,
    db: Session = Depends(get_db)
):
    return HabitService.delete_habit_by_id(db,habit_id)