
# 🧭 Camp Navigator: RAG Assistant (Flask + FAISS + Akash-Ready)

Welcome to the **Artemis Camp Navigator**, a no-touch, student-friendly Retrieval-Augmented Generation (RAG) assistant built for deployment on the decentralized **Akash Cloud**.

This project teaches how to combine:
- 🧠 vector search (FAISS)
- 🤖 open-source LLMs (Mistral 7B)
- 🔐 student-aware endpoint security
- 📦 decentralized blockchain-enabled deployment (Akash)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

---

## 🧠 What Does It Do?

This app:
- Generates daily mission directives for students
- Answers questions about camp material using embedded source files
- Runs with **zero maintenance** after deployment (🔥 “no-touch” mode)

---

## 🧩 Core Technologies

| Component          | Description                               |
|--------------------|-------------------------------------------|
| `Flask`            | Lightweight REST API framework            |
| `FAISS`            | Fast vector search over chunked docs      |
| `Mistral 7B`       | Open LLM from Hugging Face (via `transformers`) |
| `SentenceTransformers` | MiniLM-based embeddings                |
| `Akash Network`    | GPU hosting and decentralized compute     |

---

## 🔐 Security Overview

- 50 pre-registered student accounts (e.g. `student01` to `student50`)
- Each student must use a token (e.g. `pass01`)
- API endpoints are **read-only**:
  - No uploads
  - No retraining
  - No admin access

> No `.env` required or editable once deployed. All configs are baked in.

---

## 🚀 API Endpoints (Usage)

| Endpoint | Description |
|----------|-------------|
| `/api/daily_directive?student_id=X&token=Y` | Returns a short mission directive |
| `/api/ask?student_id=X&token=Y&q=YOUR+QUESTION` | General-purpose RAG query |

Example:

```

[https://YOUR-AKASH-URL/api/daily\_directive?student\_id=student05\&token=pass05](https://YOUR-AKASH-URL/api/daily_directive?student_id=student05&token=pass05)
[https://YOUR-AKASH-URL/api/ask?student\_id=student05\&token=pass05\&q=What](https://YOUR-AKASH-URL/api/ask?student_id=student05&token=pass05&q=What) is FSM?

````

---

## 🧠 MCP/FSM Process Overview

This assistant is structured using the **MCP Loop (Sense → Plan → Act → Log → Repeat)** + FSM pattern:

```mermaid
graph TD
    A[📥 Student Query] --> B[🔍 Embed Input]
    B --> C[🧠 Search FAISS Index]
    C --> D[🪄 Prompt Engineering]
    D --> E[🗣️ Mistral Generates Response]
    E --> F[📤 Return JSON to Student]
````

* **Sense:** Embed the question with MiniLM
* **Plan:** Compare to pre-indexed camp materials
* **Act:** Pass top matches as prompt to the model
* **Log:** Return answer and context snippet

---

## 📁 Folder Structure

```
my-flask-rag-app/
├── app/
│   ├── __init__.py           # Flask app factory
│   ├── routes.py             # Auth + RAG endpoints
│   └── rag_utils.py          # FAISS + LLM functions
├── templates/
│   └── index.html            # Simple landing page
├── docs/                     # Your markdown/txt content
├── faiss.index               # Vector search index (auto-generated)
├── embeddings.json           # Metadata for chunked vectors
├── prep_index.py             # Script to build index
├── requirements.txt
├── Dockerfile
├── wsgi.py
├── deploy.yaml               # Akash SDL file
├── README.md                 # You're reading it
└── README_DEPLOY.md          # Full deployment guide
```

---

## 🛠️ Developer Tips (Offline Testing)

To rebuild the vector index locally:

```bash
python prep_index.py
```

To test locally (not on Akash):

```bash
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
```

[Other Useful Deployment Notes](README_DEPLOY>MD)

---

## ⛓️ Blockchain + Funding Requirements

> ⚠️ Deployment requires **AKT tokens** and a valid Akash wallet.

You can fund your wallet using:

* 🧬 [Keplr Wallet + Osmosis DEX](https://app.osmosis.zone/)
* 💵 [Coinbase → Cosmos → Osmosis → Akash](https://akash.network/blog)

See the detailed guide here:
📘 [`FUNDING_AKASH_WALLET.md`](FUNDING_AKASH_WALLET.md)

---

## 🎓 Educational Extensions

Students can:

* Create new documents (`docs/*.md`) to teach the model new things
* Use `/api/ask` to query historical camp material
* Study FSM and prompt design patterns in `rag_utils.py`

## 🤝 Funded in Part by:

> **Albany State University Center for Blockchain Innovation and Emerging Technology**
> Supported this work to advance open-source, student-facing applications that explore:
>
> * Decentralized AI pipelines
> * Blockchain-secured infrastructure
> * Education through responsible deployment models 

---

## 🌐 What Is the Akash Cloud?

The **Akash Cloud** is a decentralized, open-source cloud computing marketplace built on the **Cosmos blockchain ecosystem**. It allows users to deploy applications (like websites, AI models, or full containers) on underutilized compute infrastructure contributed by a global network of providers.


| Feature                | Description                                                                |
| ---------------------- | -------------------------------------------------------------------------- |
| **Decentralized**      | No central cloud authority (unlike AWS, GCP, Azure)                        |
| **Blockchain-secured** | Uses the **Akash blockchain** to manage leases, payments, and resources    |
| **Token-Powered**      | Payment is made in **AKT tokens**, Akash’s native utility token            |
| **Open-Access**        | Anyone can offer compute or deploy workloads using Docker-based containers |
| **Part of Cosmos**     | Built with the Cosmos SDK, interoperable with other IBC-enabled chains     |

---

## 🧠 Why Use Akash for AI + RAG?

The Akash Cloud is ideal for AI projects like yours because:

* ✅ It supports **GPU and CPU workloads**
* ✅ You **retain full control** of your container (no vendor lock-in)
* ✅ You can **automate deployment** with YAML + CLI (`deploy.yaml`, `deploy.sh`)
* ✅ It's significantly more **cost-efficient** for persistent, low-maintenance apps

---

## 📎 Useful References

* 🌐 [Akash Network Homepage](https://akash.network)
* 📘 [Akash Docs – Get Started](https://docs.akash.network/)
* 💰 [Tips, Tricks, and Traps for ESP32 AI Agent Systems](https://github.com/RudyMartin/esp32-ai-agents) – Build Smarter Devices with the MCP/FSM Method
* 🧠 [CodeBreakers Manifesto](terms/CodeBreakers_Manifesto.md) – Responsible tech principles

---

## 📜 License

This project is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. You are free to **share**, **remix**, and **build upon** this work—even commercially—as long as you give proper credit.

---

**Built with ❤️ using [CodeBreakers](terms/CodeBreakers_Manifesto.md) / Next Shift Consulting**



