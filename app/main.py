# app/main.py

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
def ui():
    return """
    <html>
      <head>
        <title>Banking77 Intent Demo</title>
      </head>
      <body>
        <h1>Banking77 Intent API – Demo</h1>
        <form id="form">
          <textarea id="text" rows="4" cols="60"
            placeholder="Írd ide az angol nyelvű ügyfélüzenetet..."></textarea><br/>
          <button type="button" onclick="send()">Küldés</button>
        </form>
        <pre id="result"></pre>

        <script>
          async function send() {
            const text = document.getElementById('text').value;
            const response = await fetch('/predict', {
              method: 'POST',
              headers: {'Content-Type': 'application/json'},
              body: JSON.stringify({text})
            });
            const data = await response.json();
            document.getElementById('result').textContent = JSON.stringify(data, null, 2);
          }
        </script>
      </body>
    </html>
    """
