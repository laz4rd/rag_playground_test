from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from rag_chat import ask_question
from ingest import ingest_pdf
import os

app = FastAPI()

DOCUMENTS_DIR = "documents"

os.makedirs(DOCUMENTS_DIR, exist_ok=True)


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {"status": "online"}


@app.post("/chat")
def chat_endpoint(request: ChatRequest):

    result = ask_question(request.question)

    return {
        "answer": result["answer"],
        "sources": len(result["chunks"])
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(
        DOCUMENTS_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    chunk_count = ingest_pdf(file_path)

    return {
        "status": "success",
        "filename": file.filename,
        "chunks": chunk_count
    }

@app.get("/documents")
def get_documents():

    files = [
        file
        for file in os.listdir(DOCUMENTS_DIR)
        if file.endswith(".pdf")
    ]

    return {
        "documents": files
    }