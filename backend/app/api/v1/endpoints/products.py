from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db import models
from app.schemas import product as schemas
from app.services import storage, vision 

router = APIRouter()

@router.post("/process", response_model=schemas.ProductResponse)
async def process_product_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Le fichier doit être une image.")

    try:
        # 1. Lire le fichier en mémoire (bytes)
        file_content = await file.read()

        # 2. Upload de l'image ORIGINALE (Raw)
        original_url = storage.upload_image_to_cloud(file_content, f"raw_{file.filename}")
        
        # 3. TRAITEMENT IA (Détourage)
        # On passe les bytes à notre service d'IA
        processed_content = vision.remove_background(file_content)
        
        clean_filename = f"clean_{file.filename.split('.')[0]}.png"
        processed_url = storage.upload_image_to_cloud(processed_content, clean_filename)
        
        new_product = models.Product(
            filename=file.filename,
            original_image_url=original_url,
            processed_image_url=processed_url, 
            tags=None,
            description=None
        )
        
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        
        return new_product

    except Exception as e:
        print(f"Erreur lors du traitement: {e}")
        raise HTTPException(status_code=500, detail=f"Erreur interne: {str(e)}")