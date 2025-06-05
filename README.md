# rag-demo
Data Science Camp Navigator
# 🔍 Ask the Camp: RAG Demo (Streamlit + FAISS + Open LLM)

Welcome to the **CodeBreakers RAG Demo**, a student-friendly starter project that teaches how to build an AI assistant using Retrieval-Augmented Generation (RAG).
This project reflects the values in the [CodeBreakers Manifesto](../codebreakers_manifesto)—open, ethical, user-first technology.

![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)

## 🧠 What Is This?

This is a **question-answering assistant** built with:

* 🧱 **Streamlit** – Easy UI for chatting with the assistant
* 🔍 **FAISS** – Fast similarity search engine to retrieve relevant text chunks
* 🤖 **Hugging Face LLM** – Open-source language model for generating answers

## 📁 Folder Structure

```
rag-demo/
├── app.py                # Main Streamlit app
├── docs/                 # Your data source (camp handouts, README files, etc.)
├── faiss.index           # Auto-generated FAISS index file
├── embeddings.json       # Embedding metadata for each chunk
├── requirements.txt      # Python dependencies
└── README.md             # You're reading it!
```

## 🚀 How to Run (Local)

1. **Clone the repo**

   ```bash
   git clone https://github.com/YOUR-ORG/rag-demo.git
   cd rag-demo
   ```

2. **Install dependencies** (recommended: use a virtualenv)

   ```bash
   pip install -r requirements.txt
   ```

3. **Add documents**
   Drop `.txt` or `.md` files into the `docs/` folder (e.g., camp schedule, tutorials).

4. **Launch the app**

   ```bash
   streamlit run app.py
   ```

5. Ask it anything! Example: *"What are students doing on Day 2?"*

## 🧠 How It Works (Architecture)

```
           ┌──────────────────────────┐
           │   Student Question  │
           └───────────────────────┘
                    │
                    ▼
        ┌────────────────────────────┐
        │ Embed question using model │◄──────────────────────┐
        └─────────────────────────┘             │
                 │                                 │
                 ▼                                 │
        ┌───────────────────────────┐             │
        │   Search similar chunks    │             │
        │      using FAISS index     │             │
        └─────────────────────────┘             │
                 │                                 │
                 ▼                                 │
        ┌───────────────────────────┐             │
        │   Construct prompt:        │             │
        │   [Context + Question]     │             │
        └─────────────────────────┘             │
                 │                                 │
                 ▼                                 │
        ┌───────────────────────┐             │
        │     Generate answer         │◄──────────────────┐
        │     with open-source LLM    │
        └───────────────────────┘
                 │
                 ▼
        ┌───────────────────────┐
        │   Display answer + context │
        └───────────────────────┘
```

## 🎓 Student Challenges

* 🔧 Add a new document (e.g., team instructions)
* 🧪 Improve chunking logic (e.g., by section headings)
* 🔍 Let users see how the retrieved chunks impact the answer
* 🤖 Replace model with local LLM (e.g., using [Ollama](https://ollama.ai/))
* 💬 Add a feedback button ("Was this answer helpful?")

## 📜 License

This project is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. You are free to **share**, **remix**, and **build upon** this work—even commercially—as long as you give proper credit.

Learn more: [https://creativecommons.org/licenses/by/4.0](https://creativecommons.org/licenses/by/4.0)

You may also add this badge to your GitHub project:

```markdown
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
```

---

**Built with ❤️ by CodeBreakers / Next Shift Consulting**
Join the movement → [CodeBreakers Manifesto](../codebreakers_manifesto)
