from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import summarize_incident_tool

app = FastAPI()

class IncidentRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Industrial Incident ADK Agent Running"}

@app.get("/health")
def health():
    return {"status": "running"}

@app.post("/summarize")
def summarize(request: IncidentRequest):
    result = summarize_incident_tool(request.text)
    return {"summary": result}