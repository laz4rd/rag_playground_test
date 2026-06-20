from ollama import chat
from pdf_read import extract_pdf_text


pdf_text = extract_pdf_text("documents/sample.pdf")



print(f"PDF Extraction: {pdf_time:.2f}s")
print(f"Characters: {len(pdf_text)}")
print(f"Words: {len(pdf_text.split())}")

question = input("\nAsk a question: ")


response = chat(
    model="gemma4:31b-cloud",
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




print(response["message"]["content"])
