import faiss
import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline, PipelineException
from sklearn.metrics.pairwise import cosine_similarity

MODEL_READY = False
try:
    embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    llm = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1", device=-1)
    MODEL_READY = True
except Exception as e:
    print(f"❌ Model initialization failed: {e}")

index_path = "faiss.index"
embeddings_path = "embeddings.json"

if MODEL_READY:
    try:
        with open(embeddings_path, "r") as f:
            docs = json.load(f)
        index = faiss.read_index(index_path)
    except Exception as e:
        print(f"❌ FAISS loading failed: {e}")
        MODEL_READY = False
else:
    docs = []
    index = None

def query_rag(user_input, k=3):
    query_vec = embedder.encode([user_input])
    D, I = index.search(np.array(query_vec), k)
    context = "\n".join([docs[i]['text'] for i in I[0]])
    prompt = f"Context:\n{context}\n\nQuestion: {user_input}\nAnswer:"
    result = llm(prompt, max_new_tokens=150, do_sample=False)
    return result[0]['generated_text'].replace(prompt, ''), context
