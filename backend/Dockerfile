FROM python:3.10-slim

# Empêche Python d'écrire des fichiers .pyc (inutiles dans un conteneur)
ENV PYTHONDONTWRITEBYTECODE=1
# Force Python à afficher les logs en temps réel (crucial pour le débogage Docker)
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc python3-dev libpq-dev \
    && apt-get clean

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]