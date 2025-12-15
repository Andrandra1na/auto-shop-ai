from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# 1. Création du moteur (Le lien physique avec la DB)
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

# 2. Création de l'usine à sessions (Pour créer des connexions à la demande)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. La classe de base pour nos modèles (Tous nos modèles hériteront de ça)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()