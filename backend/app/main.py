from fastapi import FastAPI
from app.db.session import engine, Base
from app.api.v1.endpoints import products 

# Création des tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Auto-Shop AI API",
    description="API d'automatisation e-commerce alimentée par l'IA.",
    version="1.0.0"
)


app.include_router(products.router, prefix="/api/v1/products", tags=["Products"])

@app.get("/")
async def root():
    return {"message": "Auto-Shop AI API is running", "db_status": "connected"}