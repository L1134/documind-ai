from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="DocuMind AI API")

class Question(BaseModel):
    query: str

@app.get("/")
def root():
    return {"message": "DocuMind AI API is running"}

@app.post("/ask")
def ask(question: Question):
    return {
        "question": question.query,
        "answer": "This is a placeholder response from DocuMind AI."
    }
