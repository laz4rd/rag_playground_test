import time
from ollama import chat
from pdf_read import extract_pdf_text

# Measure PDF extraction time
start = time.time()

pdf_text = extract_pdf_text("documents/sample.pdf")

pdf_time = time.time() - start

print(f"PDF Extraction: {pdf_time:.2f}s")
print(f"Characters: {len(pdf_text)}")
print(f"Words: {len(pdf_text.split())}")

question = input("\nAsk a question: ")

# Measure LLM response time
start = time.time()

response = chat(
    model="qwen3:8b",
    messages=[
        {
            "role": "system",
            "content": f"""
You are a study assistant.

Answer only using the provided document.

DOCUMENT:

{pdf_text}
"""
        },
        {
            "role": "user",
            "content": question
        }
    ]
)

llm_time = time.time() - start

print(f"\nLLM Response Time: {llm_time:.2f}s\n")
print(response["message"]["content"])
