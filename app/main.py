from fastapi import FastAPI
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
