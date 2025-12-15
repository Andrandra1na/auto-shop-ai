from fastapi import FastAPI
from app.db.session import engine, Base
from app.db import models 

# Création automatique des tables dans la DB au démarrage
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Auto-Shop AI API",
    description="API d'automatisation e-commerce alimentée par l'IA.",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Auto-Shop AI API is running", "db_status": "connected"}