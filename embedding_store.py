#import chromadb
from sentence_transformers import SentenceTransformer
import chromadb
import pandas as pd

def create_vector_store(file_path=r"C:\Users\grewa\p_AI\data\issue_log (1).xlsx"):
    df = pd.read_excel(file_path)
    df['combined_text'] = (
        "Issue: " + df['Issue_Description'].fillna('') + " | " +
        "Root Cause: " + df['Root_Cause'].fillna('') + " | " +
        "Resolution: " + df['Resolution_Steps'].fillna('') + " | " +
        "Learnings: " + df['Learnings'].fillna('')
    )
    model = SentenceTransformer('all-MiniLM-L6-v2')
    chroma_client = chromadb.Client()
    collection = chroma_client.create_collection(name="issues")

    for i, row in df.iterrows():
        emb = model.encode(row['combined_text']).tolist()
        collection.add(
            documents=[row['combined_text']],
            embeddings=[emb],
            ids=[row['Issue_ID']],
            metadatas=[{"System_Component": row["System_Component"], "Severity": row["Severity"]}]
        )
    print("✅ Embeddings created successfully.")
    return collection

if __name__ == "__main__":
    create_vector_store()
