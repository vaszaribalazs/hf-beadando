from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from .model import predict_intent

app = FastAPI(title="Banking77 Intent API", version="1.0.0")

class TextIn(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Banking77 Intent API működik. Használd a POST /predict végpontot."}

@app.post("/predict")
def predict(payload: TextIn):
    return predict_intent(payload.text)

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
