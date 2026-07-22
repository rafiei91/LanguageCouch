from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.root import router as root_router

app = FastAPI(
    title="LanguageCouch API",
    description="Backend API for LanguageCouch",
    version="0.1.0",
)

app.include_router(root_router)
app.include_router(health_router)