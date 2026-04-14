import numpy as np

stored_data = []

def store_embeddings(chunks, embeddings):
    global stored_data
    stored_data = []

    for i, emb in enumerate(embeddings):
        stored_data.append({
            "embedding": emb,
            "text": chunks[i]
        })


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def search_embeddings(query_embedding, top_k=3):
    scores = []

    for item in stored_data:
        score = cosine_similarity(query_embedding, item["embedding"])
        scores.append((score, item["text"]))

    scores.sort(reverse=True)
    return [text for _, text in scores[:top_k]]