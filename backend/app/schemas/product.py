from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Dict

class ProductResponse(BaseModel):
    id: int
    filename: str
    original_image_url: Optional[str] = None
    processed_image_url: Optional[str] = None
    tags: Optional[List[str] | Dict] = None
    description: Optional[str] = None
    created_at: datetime

    class Config:
        # Permet à Pydantic de lire les données directement depuis l'objet SQLAlchemy
        from_attributes = True