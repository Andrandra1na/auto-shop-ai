from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db import models
from app.schemas import product as schemas
from app.services import storage

router = APIRouter()

@router.post("/process", response_model=schemas.ProductResponse)
async def process_product_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    Reçoit une image, l'envoie sur le Cloud, et crée l'entrée en base de données.
    Pour l'instant, on ne fait que l'upload (pas encore d'IA).
    """
    # 1. Validation basique
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Le fichier doit être une image.")

    try:
        # 2. Upload vers Cloudinary
        # On utilise file.file qui est l'objet binaire
        image_url = storage.upload_image_to_cloud(file.file, file.filename)
        
        # 3. Création de l'objet en Base de Données
        new_product = models.Product(
            filename=file.filename,
            original_image_url=image_url,
            # Pour l'instant, pas d'IA, donc on laisse le reste vide
            processed_image_url=None,
            tags=None,
            description=None
        )
        
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        
        return new_product

    except Exception as e:
        print(f"Erreur lors du traitement: {e}")
        raise HTTPException(status_code=500, detail="Erreur interne lors de l'upload")