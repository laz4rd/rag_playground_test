from embedder import get_embedding
from vector_store import search

question = input("Question: ")

question_embedding = get_embedding(question)

results = search(question_embedding)

print("\nTop Results:\n")

for i, chunk in enumerate(results):
    print(f"\n--- Result {i+1} ---\n")
    print(chunk[:800])