from openai import AsyncOpenAI
from app.core.config import settings

client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.OPENROUTER_API_KEY,
)

async def generate_product_description(product_name: str) -> str:
    clean_name = product_name.replace("_", " ").replace("-", " ").split(".")[0]

    prompt = f"""
    Tu es un expert en copywriting E-commerce.
    Rédige une description produit séduisante, professionnelle et optimisée pour le SEO pour l'article suivant : "{clean_name}".
    
    Structure de la réponse :
    1. Une accroche percutante.
    2. Une liste de 3 points forts probables (imagine-les de manière réaliste basés sur le nom).
    3. Une conclusion invitant à l'achat.
    
    Réponds uniquement en Français. N'ajoute pas de guillemets autour de la réponse.
    """

    try:
        response = await client.chat.completions.create(
            model=settings.OPENROUTER_MODEL,
            messages=[
                {"role": "system", "content": "Tu es un assistant expert en vente en ligne."},
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Erreur LLM: {e}")
        return "Description indisponible pour le moment."