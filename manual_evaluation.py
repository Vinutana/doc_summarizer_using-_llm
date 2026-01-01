from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

def semantic_score(reference, generated):
    ref_emb = model.encode([reference])
    gen_emb = model.encode([generated])
    return cosine_similarity(ref_emb, gen_emb)[0][0]

ref = "Machine learning is a subset of AI that learns from data."
gen = "ML is part of AI and it trains on data."
print("Similarity:", semantic_score(ref, gen))
