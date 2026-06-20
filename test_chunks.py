from pdf_read import extract_pdf_text
from chunker import create_chunks

text = extract_pdf_text("documents/sample.pdf")

chunks = create_chunks(text)

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks[:3]):
    print(f"\n--- Chunk {i+1} ---")
    print(chunk[:500])