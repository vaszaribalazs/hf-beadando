FROM python:3.11-slim

# Rendszer csomagok
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Python csomagok
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Alkalmazás fájlok
COPY app /app/app
COPY data /app/data

# A Hugging Face 7860-as portot vár – állítsuk be és használjuk
ENV PORT=7860

CMD ["bash", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
