from sqlalchemy.orm import Session

from app.models.habit import Habit
from app.schemas.habit import HabitCreate


class HabitService:

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
    def get_all_habits(db: Session) -> list[Habit]:
        return db.query(Habit).all()
