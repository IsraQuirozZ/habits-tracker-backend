from fastapi import APIRouter
from app.api.v1.habits import router as habits_router

api_router = APIRouter(prefix="/api")

api_router.include_router(habits_router)

# Aquí se irán incluyendo las versiones
# api_router.include_router(v1_router)
