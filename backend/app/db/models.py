from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.sql import func
from app.db.session import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    
    # Métadonnées de l'image
    filename = Column(String, nullable=False)
    
    # URLs des images (stockées sur Cloudinary plus tard)
    original_image_url = Column(String, nullable=True)
    processed_image_url = Column(String, nullable=True) # L'image détourée
    
    # Données IA
    tags = Column(JSON, nullable=True) # Liste de tags (ex: ["Nike", "Rouge"])
    description = Column(Text, nullable=True) # Description générée par LLM
    
    # Audit
    created_at = Column(DateTime(timezone=True), server_default=func.now())