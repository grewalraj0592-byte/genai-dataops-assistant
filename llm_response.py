from openai import OpenAI
from embedding_store import create_vector_store

def generate_llm_response(query_text):
    client = OpenAI(api_key="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")
    collection = create_vector_store()
    results = collection.query(query_texts=[query_text], n_results=3)
    context = "\n\n".join(results["documents"][0])
    prompt = f"""
    You are a DataOps assistant. Given the following historical issues, 
    suggest a resolution for this new query.

    Query: {query_text}
    Context: {context}
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    print("Assistant Suggestion:\n", response.choices[0].message.content)

if __name__ == "__main__":
    generate_llm_response("PySpark masking issue in production job")

