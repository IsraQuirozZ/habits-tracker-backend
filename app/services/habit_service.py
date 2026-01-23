from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.habit import Habit
from app.schemas.habit import HabitCreate, HabitUpdate


class HabitService:

    @staticmethod
    def get_all_habits(db: Session) -> list[Habit]:
        habits = db.query(Habit).all()
        if not habits:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No hay Habitos registrados"
            )
        return habits

    @staticmethod
    def get_habit_by_id(db: Session, habit_id: int) -> Habit:
        habit = db.query(Habit).filter(Habit.id == habit_id).first()

        if not habit:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Hábito no encontrado"
            )

        return habit

    @staticmethod
    def create_habit(db: Session, habit_data: HabitCreate) -> Habit:
        habit = Habit(
            name=habit_data.name,
            description=habit_data.description,
        )

        db.add(habit)
        db.commit()
        db.refresh(habit)

        return habit

    @staticmethod
    def update_habit_by_id(db: Session, habit_id: int, habit_data: HabitUpdate) -> Habit:
        habit = db.query(Habit).filter(Habit.id == habit_id).first()

        if not habit:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Hábito no encontrado"
            )
        
        if habit_data.name is not None:
            habit.name = habit_data.name
        
        if habit_data.description is not None:
            habit.description = habit_data.description

        db.commit()
        db.refresh(habit)

        return habit
    
    @staticmethod
    def delete_habit_by_id(db:Session, habit_id:int) -> Habit:
        habit = db.query(Habit).filter(Habit.id == habit_id).first()

        if not habit:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Hábito no encontrado"
            )
        
        db.delete(habit)
        db.commit()

        return habit


 