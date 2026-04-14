""" from fastapi import FastAPI
from .utils import load_pdf, chunk_text
from .embeddings import get_embeddings
from .database import store_embeddings, search_embeddings

from .rag import generate_answer

from backend.utils import load_pdf, chunk_text
from backend.embeddings import get_embeddings
from backend.database import store_embeddings, search_embeddings
from backend.rag import generate_answer

app = FastAPI()

@app.get("/")
def home():
    return {"message": "RAG Chatbot API running"}

@app.post("/process")
def process_pdf():
    text = load_pdf("data/sample.pdf")
    chunks = chunk_text(text)
    embeddings = get_embeddings(chunks)

    store_embeddings(chunks, embeddings)

    return {"message": "PDF processed and stored in Endee"}

@app.get("/ask")
def ask(query: str):
    query_embedding = get_embeddings([query])[0]
    context = search_embeddings(query_embedding)

    answer = generate_answer(query, context)
    return {"answer": answer} """



from fastapi import FastAPI, UploadFile, File
import shutil
import os

from backend.utils import load_pdf, chunk_text
from backend.embeddings import get_embeddings
from backend.database import store_embeddings, search_embeddings
from backend.rag import generate_answer

app = FastAPI()

UPLOAD_PATH = "data/uploaded.pdf"

@app.get("/")
def home():
    return {"message": "RAG Chatbot API running"}


@app.post("/upload")
def upload_pdf(file: UploadFile = File(...)):
    # Save uploaded file
    with open(UPLOAD_PATH, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process PDF
    text = load_pdf(UPLOAD_PATH)
    chunks = chunk_text(text)
    embeddings = get_embeddings(chunks)

    store_embeddings(chunks, embeddings)

    return {"message": "PDF uploaded and processed"}


@app.get("/ask")
def ask(query: str):
    query_embedding = get_embeddings([query])[0]
    context = search_embeddings(query_embedding)

    answer = generate_answer(query, context)
    return {"answer": answer}