import chromadb

def query_issue(collection, query_text):
    results = collection.query(query_texts=[query_text], n_results=3)
    for i, doc in enumerate(results["documents"][0]):
        print(f"\nMatch {i+1}: {doc}\n")

if __name__ == "__main__":
    from embedding_store import create_vector_store
    collection = create_vector_store()
    query = "Snowflake masking issue causing null data in reports"
    query_issue(collection, query)
