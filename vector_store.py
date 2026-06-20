import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="documents"
)

def add_chunk(chunk_id, chunk_text, embedding):

    collection.add(
        ids=[str(chunk_id)],
        documents=[chunk_text],
        embeddings=[embedding]
    )
    
def search(query_embedding, n_results=4):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results["documents"][0]