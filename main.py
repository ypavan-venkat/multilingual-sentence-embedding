from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading model...")

model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

print("Model loaded successfully!\n")

sentences = [
    "I love artificial intelligence.",
    "मुझे कृत्रिम बुद्धिमत्ता पसंद है।",
    "నాకు కృత్రిమ మేధస్సు ఇష్టం.",
    "I play cricket every day."
]

embeddings = model.encode(sentences)

similarity_matrix = cosine_similarity(embeddings)

print("Similarity Matrix:\n")

for i in range(len(sentences)):
    for j in range(len(sentences)):
        print(f"{similarity_matrix[i][j]:.4f}", end="  ")
    print()