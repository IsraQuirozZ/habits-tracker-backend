from fastapi import APIRouter

api_router = APIRouter(prefix="/api")

# Aquí se irán incluyendo las versiones
# api_router.include_router(v1_router)
