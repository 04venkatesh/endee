import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_answer(query, context_chunks):
    context = "\n".join(context_chunks)

    prompt = f"""
Answer ONLY using the context below.
If not found, say "Not in document".

Context:
{context}

Question:
{query}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    # 🔥 SAFE handling (fix error)
    return data.get("response", "Error: No response from model")