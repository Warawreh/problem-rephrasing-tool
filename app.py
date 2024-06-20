from rephrase_model import *
from fastapi import FastAPI, HTTPException, Query, Request
from typing import List
from helpers import *

# run API with uvicorn app:app --reload

app = FastAPI()
rephrase = Rephraser()

@app.get("/rephrase")
def rephrase_text(texts: List[str] = Query(...)):
    texts = [clean_html_tags(text) for text in texts]

    quran_hadeeth_texts = [text for text in texts if check_quran_phrases_and_hadeeth(text)]
    other_texts = [text for text in texts if text not in quran_hadeeth_texts]

    res = [rephrase.rephrase(text) for text in other_texts]
    res.extend(quran_hadeeth_texts)
    
    return res