# server.py
from fastapi import FastAPI
import torch
from pydantic import BaseModel
app = FastAPI()

class Req(BaseModel):
    text: str

# Example: small torch model (replace with real model in POC)
model = None
@app.on_event("startup")
def load_model():
    global model
    # Replace with loading of your actual model; use .to(device)
    model = torch.nn.Linear(10, 1)
    model.eval()

@app.post("/predict")
def predict(req: Req):
    # Dummy numeric transform — replace with real preprocessing
    x = torch.randn(1, 10)
    with torch.no_grad():
        out = model(x)
    return {"result": out.tolist()}
