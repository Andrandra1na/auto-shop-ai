from rembg import remove
from PIL import Image
import io

def remove_background(image_bytes: bytes) -> bytes:
    """
    Prend les octets d'une image brute, supprime le fond via IA,
    et retourne les octets de l'image détourée (format PNG).
    """
    try:
        output_image = remove(image_bytes)
        
        
        # On convertit les octets en objet Image pour vérifier
        img = Image.open(io.BytesIO(output_image))
        
        # On prépare un buffer pour ré-écrire l'image en octets
        output_buffer = io.BytesIO()
        img.save(output_buffer, format="PNG")
        
        return output_buffer.getvalue()

    except Exception as e:
        print(f"Erreur AI Vision: {e}")
        raise e