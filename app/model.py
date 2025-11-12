from pathlib import Path
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Adatok betöltése
BASE_DIR = Path(__file__).resolve().parents[1]
TRAIN_PATH = BASE_DIR / "data" / "banking77_train_sample.csv"

train_df = pd.read_csv(TRAIN_PATH)
INTENT_LABELS = sorted(train_df["label"].unique().tolist())

# Modell inicializálása
MODEL_NAME = "facebook/bart-large-mnli"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

classifier = pipeline(
    task="zero-shot-classification",
    model=model,
    tokenizer=tokenizer,
    device=-1  # CPU-n fut
)

def predict_intent(text: str) -> dict:
    """Intent osztályozás Banking77 adatokkal"""
    result = classifier(text, candidate_labels=INTENT_LABELS, multi_label=False)
    return {
        "text": text,
        "intent": result["labels"][0],
        "score": float(result["scores"][0]),
        "all_labels": result["labels"],
        "all_scores": [float(s) for s in result["scores"]],
    }
