from ollama import chat

from embedder import get_embedding
from vector_store import search
import time

question = input("Question: ")

# Embed the question
question_embedding = get_embedding(question)

# Retrieve relevant chunks
chunks = search(question_embedding)

# Combine chunks into context
context = "\n\n".join(chunks)

print("\nRetrieved Context Length:", len(context))

start = time.time()

response = chat(
    model="gemma4:31b-cloud",
    messages=[
        {
            "role": "system",
            "content": f"""
You are a study assistant.

Answer ONLY using the provided context.

If the answer is not present in the context,
say:

"I could not find that information in the document."

CONTEXT:

{context}
"""
        },
        {
            "role": "user",
            "content": question
        }
    ]
)

print("\nAnswer:\n")
print(response["message"]["content"])
print("\nRetrieved Chunks:\n")

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---")
    print(chunk[:300])