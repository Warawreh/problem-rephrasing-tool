from rephrase_model import *
from fastapi import FastAPI, HTTPException, Query, Request
from typing import List

# run API with uvicorn app:app --reload

app = FastAPI()
rephrase = Rephraser()

@app.get("/rephrase")
def rephrase_text(texts: List[str] = Query(...)):
    return [rephrase.rephrase(text) for text in texts]