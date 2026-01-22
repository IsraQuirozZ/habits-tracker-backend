from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(
    title="Habits Tracker API",
    version="0.1.0",
)

app.include_router(api_router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
