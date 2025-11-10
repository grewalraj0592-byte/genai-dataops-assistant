from fastapi import FastAPI
from embedding_store import create_vector_store

app = FastAPI()
collection = None

@app.post("/train")
def train_model():
    global collection
    collection = create_vector_store()
    return {"message": "Embeddings created successfully."}

@app.get("/query")
def get_resolution(query: str):
    global collection
    if not collection:
        collection = create_vector_store()
    results = collection.query(query_texts=[query], n_results=3)
    return {"query": query, "results": results["documents"][0]}
