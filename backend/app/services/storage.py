import cloudinary
import cloudinary.uploader
from app.core.config import settings

# Configuration initiale de la librairie
cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET,
    secure=True
)

def upload_image_to_cloud(file_file, filename: str) -> str:
    """
    Envoie une image vers Cloudinary et retourne son URL sécurisée (https).
    
    :param file_file: Le fichier binaire reçu par l'API
    :param filename: Le nom qu'on veut donner au fichier (public_id)
    :return: L'URL de l'image stockée
    """
    try:
        # Cloudinary gère l'upload
        response = cloudinary.uploader.upload(
            file_file,
            public_id=filename,
            unique_filename=True,
            overwrite=True
        )
        return response.get("secure_url")
    except Exception as e:
        print(f"Erreur Upload Cloudinary: {e}")
        raise e