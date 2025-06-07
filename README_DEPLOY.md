
# 🚀 Akash Deployment Guide – Artemis Camp RAG App

This repository contains a fully hardened, hands-off AI assistant for students to retrieve directives and ask questions from a pre-indexed knowledge base using FAISS + Hugging Face models.

---

## ✅ What's Included

- `Flask` API with `/api/daily_directive` and `/api/ask`
- `prep_index.py` script for pre-generating `faiss.index` + `embeddings.json`
- `requirements.txt` and `Dockerfile` for Akash-ready container
- `deploy.yaml` (Akash SDL) and `deploy.sh` (automated CLI deployment)

---

## 🔐 Access Rules

- 50 hardcoded student IDs (`student01`–`student50`)
- Each student must provide a valid `token` (e.g. `pass01`) in the URL
- No dynamic config, no runtime modification, no admin backdoor

---

## 📦 Build and Push to DockerHub

```bash
docker build -t yourname/my-flask-rag-app .
docker push yourname/my-flask-rag-app
```

---

## 🌍 Deploy on Akash

1. Replace values in `deploy.yaml`
   - Docker image name
   - Akash wallet address

2. Run the script:

```bash
chmod +x deploy.sh
./deploy.sh
```

3. Open the URL from `lease-status` to access your app.

---

## 📘 Example Usage

```bash
curl 'https://yourapp.aksh.net/api/daily_directive?student_id=student01&token=pass01'
```

---

## 🧠 Index New Documents

To update the underlying knowledge base:

```bash
# Add .md or .txt files to /docs
python prep_index.py
```

⚠️ Requires container rebuild + redeployment.

---

## 🧯 Fail-Safe Behavior

- If the model or index fails to load → `503`
- If the token is invalid or missing → `403`
- If a query throws an exception → `500`
- No backend shell or runtime write access is exposed

---

Maintained for the 2025 Artemis Generative AI Camp.
