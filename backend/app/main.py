from fastapi import FastAPI

app = FastAPI(
    title="LanguageCouch API",
    description="Backend API for LanguageCouch",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "Welcome to LanguageCouch API"}

@app.get("/health")
def health():
    return {"status": "healthy"}