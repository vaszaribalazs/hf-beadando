# Python 3.11 slim image
FROM python:3.11-slim

# Rendszer csomagok, amik sok libnek kellenek
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Először a requirements, hogy a pip cache réteg újrahasznosuljon
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Alkalmazás és adatok bemásolása
COPY app /app/app
COPY data /app/data

# (Opcionális) Port deklaráció
EXPOSE 8000

# Indítás: FastAPI + Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
