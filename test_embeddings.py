from pdf_read import extract_pdf_text
from chunker import create_chunks
from embedder import get_embedding

text = extract_pdf_text("documents/sample.pdf")

chunks = create_chunks(text)

print(f"Chunks: {len(chunks)}")

first_chunk = chunks[0]

embedding = get_embedding(first_chunk)

print(f"Embedding Dimensions: {len(embedding)}")
print()
print("First 10 Values:")
print(embedding[:10])