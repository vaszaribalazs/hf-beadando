# app/model.py

from transformers import pipeline

# CPU-n futó zero-shot classifier
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli",
    device=-1,  # -1 = CPU
)


INTENT_LABELS = [...]  # Banking77 címkék

def predict_intent(text: str):
    result = classifier(
        text,
        candidate_labels=INTENT_LABELS,
        multi_label=False
    )
    return {
        "text": text,
        "intent": result["labels"][0],
        "score": float(result["scores"][0]),
        "all_labels": result["labels"],
        "all_scores": [float(s) for s in result["scores"]],
    }

# <<< ITT MOST NE LEGYEN @app.get("/ui") VAGY BÁRMI, AMI APP-OT HASZNÁL >>>
