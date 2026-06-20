from pdf_read import extract_pdf_text
from chunker import create_chunks
from embedder import get_embedding
from vector_store import add_chunk

text = extract_pdf_text(
    "documents/sample.pdf"
)

chunks = create_chunks(text)

print(f"Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):

    embedding = get_embedding(chunk)

    add_chunk(
        chunk_id=i,
        chunk_text=chunk,
        embedding=embedding
    )

    print(f"Stored chunk {i}")