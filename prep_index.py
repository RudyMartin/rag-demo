import os
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

DATA_DIR = "./docs"
EMBEDDINGS_FILE = "embeddings.json"
INDEX_FILE = "faiss.index"
CHUNK_SIZE = 300

embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

docs = []
for filename in os.listdir(DATA_DIR):
    if filename.endswith(".txt") or filename.endswith(".md"):
        with open(os.path.join(DATA_DIR, filename), "r") as f:
            text = f.read()
            chunks = [text[i:i+CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]
            for c in chunks:
                docs.append({"source": filename, "text": c})

vectors = embedder.encode([d["text"] for d in docs])
index = faiss.IndexFlatL2(vectors.shape[1])
index.add(np.array(vectors))

with open(EMBEDDINGS_FILE, "w") as f:
    json.dump(docs, f)
faiss.write_index(index, INDEX_FILE)

print(f"✅ Indexed {len(docs)} chunks from {len(os.listdir(DATA_DIR))} files.")
