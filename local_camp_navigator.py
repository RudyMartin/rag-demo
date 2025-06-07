# RAG Demo Template: Streamlit + FAISS + Open-Source LLM
# --------------------------------------------------------
# This template provides a simple Retrieval-Augmented Generation (RAG) demo
# using Streamlit, FAISS for vector search, and an open-source LLM from Hugging Face.
# Designed for educational use and aligned with the CodeBreakers Manifesto.

import streamlit as st
import faiss
import os
import json
from sentence_transformers import SentenceTransformer
from transformers import pipeline
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# -------------------------
# CONFIGURATION
# -------------------------
DATA_DIR = "./docs"
INDEX_FILE = "faiss.index"
EMBEDDINGS_FILE = "embeddings.json"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
LLM_NAME = "mistralai/Mistral-7B-Instruct-v0.1"
CHUNK_SIZE = 300

# -------------------------
# LOAD MODELS
# -------------------------
st.title("🔍 Ask the Camp: RAG Demo")
@st.cache_resource
def load_models():
    embedder = SentenceTransformer(MODEL_NAME)
    llm = pipeline("text-generation", model=LLM_NAME, device=0 if torch.cuda.is_available() else -1)
    return embedder, llm

embedder, llm = load_models()

# -------------------------
# LOAD DOCUMENTS
# -------------------------
def load_docs():
    docs = []
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".txt") or filename.endswith(".md"):
            with open(os.path.join(DATA_DIR, filename), "r") as f:
                text = f.read()
                chunks = [text[i:i+CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]
                for c in chunks:
                    docs.append({"source": filename, "text": c})
    return docs

# -------------------------
# EMBEDDINGS + FAISS INDEX
# -------------------------
def build_faiss_index(docs):
    vectors = embedder.encode([d["text"] for d in docs])
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(vectors))
    with open(EMBEDDINGS_FILE, "w") as f:
        json.dump(docs, f)
    faiss.write_index(index, INDEX_FILE)
    return index, docs

if not os.path.exists(INDEX_FILE):
    st.warning("⚠️ Index not found. Building from scratch...")
    documents = load_docs()
    index, docs = build_faiss_index(documents)
else:
    index = faiss.read_index(INDEX_FILE)
    with open(EMBEDDINGS_FILE, "r") as f:
        docs = json.load(f)

# -------------------------
# RAG FUNCTION
# -------------------------
def query_rag(user_input, k=3):
    query_vec = embedder.encode([user_input])
    D, I = index.search(np.array(query_vec), k)
    context = "\n".join([docs[i]['text'] for i in I[0]])
    prompt = f"Context:\n{context}\n\nQuestion: {user_input}\nAnswer:"
    result = llm(prompt, max_new_tokens=150, do_sample=False)
    return result[0]['generated_text'].replace(prompt, ""), context

# -------------------------
# STREAMLIT UI
# -------------------------
question = st.text_input("Ask a question about the camp docs:")
if question:
    answer, retrieved = query_rag(question)
    st.subheader("📘 Retrieved Context")
    st.text(retrieved)
    st.subheader("🤖 Answer")
    st.write(answer)

    with st.expander("🔎 Show Raw Prompt"):
        st.code(f"Context:\n{retrieved}\n\nQuestion: {question}\nAnswer:")

    st.markdown("---")
    feedback = st.radio("Was this helpful?", ["👍 Yes", "👎 No"], horizontal=True)
    if feedback:
        st.success("Thanks for your feedback! Logging not yet implemented.")
