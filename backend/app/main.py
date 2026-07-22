from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="LanguageCouch API",
    description="Backend API for LanguageCouch",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "Welcome to LanguageCouch API"}

app.include_router(health_router)