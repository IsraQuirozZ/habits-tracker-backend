import logging
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.api.router import api_router
from app.core.database import Base, engine
from app.core.exceptions import validation_exception_handler
from app.models import Habit

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Habits Tracker API",
    version="0.1.0",
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

Base.metadata.create_all(bind=engine)

app.include_router(api_router)

logger = logging.getLogger(__name__)




@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
