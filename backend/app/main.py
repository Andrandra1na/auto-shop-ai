from fastapi import FastAPI

app = FastAPI(
    title="Auto-Shop AI API",
    description="API d'automatisation e-commerce alimentée par l'IA.",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Auto-Shop AI API is running", "status": "ok"}