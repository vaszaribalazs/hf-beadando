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

from fastapi.responses import HTMLResponse

@app.get("/ui", response_class=HTMLResponse)
def ui_page():
    return """
    <html>
    <head>
        <title>Banking77 Intent API – Demo</title>
    </head>
    <body style="font-family: Arial; margin: 20px">
        <h1>Banking77 Intent API – Demo</h1>
        <textarea id="inputText" rows="4" cols="80"></textarea><br><br>
        <button onclick="sendRequest()">Küldés</button>

        <h3>Eredmény:</h3>
        <pre id="output"></pre>

        <script>
            async function sendRequest() {
                const text = document.getElementById("inputText").value;

                const response = await fetch("/predict", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ text: text })
                });

                const result = await response.json();
                document.getElementById("output").textContent = JSON.stringify(result, null, 2);
            }
        </script>
    </body>
    </html>
    """
