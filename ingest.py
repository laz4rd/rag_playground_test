from pdf_read import extract_pdf_text
from chunker import create_chunks
from embedder import get_embedding
from vector_store import add_chunk


def ingest_pdf(pdf_path: str):

    text = extract_pdf_text(pdf_path)

    chunks = create_chunks(text)

    for i, chunk in enumerate(chunks):

        embedding = get_embedding(chunk)

        add_chunk(
            chunk_id=i,
            chunk_text=chunk,
            embedding=embedding
        )

    return len(chunks)