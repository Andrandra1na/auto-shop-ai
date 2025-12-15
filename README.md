# 🛍️ Auto-Shop AI

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?logo=postgresql&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit&logoColor=white)

> **L'assistant intelligent pour l'automatisation E-commerce.**
> Transformez des photos produits brutes en fiches produits professionnelles en quelques secondes grâce à l'IA Générative.

---

## 🚀 Fonctionnalités

*   **Détourage Automatique (Computer Vision) :** Suppression de l'arrière-plan avec précision grâce au modèle `U2Net` (via `rembg`).
*   **Rédaction SEO (GenAI) :** Génération automatique de descriptions marketing vendeuses basées sur le produit, propulsée par **LLaMA 3.1** (via OpenRouter).
*   **Stockage Cloud :** Hébergement sécurisé et optimisé des images via **Cloudinary**.
*   **Base de Données :** Persistance de tous les produits traités dans **PostgreSQL**.
*   **Interface Moderne :** Dashboard interactif développé avec **Streamlit** (Support du Drag & Drop, Bulk Upload, Téléchargement).

## 🏗️ Architecture Technique

Le projet suit une architecture micro-services conteneurisée :

1.  **Backend API (FastAPI) :** Gère la logique métier, l'IA et la base de données.
2.  **Database (PostgreSQL) :** Stocke les métadonnées produits et les liens images.
3.  **Frontend (Streamlit) :** Interface utilisateur connectée à l'API.
4.  **Infrastructure (Docker Compose) :** Orchestration de l'ensemble des services.

## 🛠️ Installation et Démarrage

### Pré-requis
*   Docker & Docker Compose
*   Clés API (Cloudinary & OpenRouter)

### 1. Cloner le projet

git clone https://github.com/VOTRE_NOM/auto-shop-ai.git

cd auto-shop-ai

2. Configuration

Créez un fichier .env à la racine :

# Base de données
POSTGRES_USER=autoshop_admin
POSTGRES_PASSWORD=secure_password
POSTGRES_DB=autoshop_db
POSTGRES_SERVER=db
POSTGRES_PORT=5432

# Cloudinary (Stockage Images)
CLOUDINARY_CLOUD_NAME=votre_cloud_name
CLOUDINARY_API_KEY=votre_api_key
CLOUDINARY_API_SECRET=votre_api_secret

# OpenRouter (IA Texte)
OPENROUTER_API_KEY=votre_cle_openrouter
OPENROUTER_MODEL=meta-llama/llama-3.1-8b-instruct:free

3. Lancer l'application

docker-compose up --build -d

4. Accès

Interface Utilisateur : http://localhost:8501

Documentation API (Swagger) : http://localhost:8001/docs

