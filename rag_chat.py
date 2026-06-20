from ollama import chat

from embedder import get_embedding
from vector_store import search


def ask_question(question: str):
    # Embed the question
    question_embedding = get_embedding(question)

    # Retrieve relevant chunks
    chunks = search(question_embedding)

    # Combine chunks into context
    context = "\n\n".join(chunks)

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

    return {
        "answer": response["message"]["content"],
        "chunks": chunks
    }