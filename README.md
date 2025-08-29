# RAG Doc Chat



https://github.com/user-attachments/assets/750ba8d3-0c85-4fd2-b174-40bb62fed807


A lightweight Retrieval-Augmented Generation (RAG) document chatbot that lets you **chat with your Markdown files**. Built with **Gemini API + LangChain + ChromaDB**.


This project uses the **"Alice in Wonderland"** story as a sample Markdown file to demonstrate document retrieval and querying.


---


## ✨ Features


* **Document chat**: Ask natural language questions against your Markdown files.
* **Chunking & embeddings**: Splits text and generates vector embeddings via **Gemini API**.
* **Persistent vector store**: Uses **ChromaDB** (local, fast) with `persist_directory`.
* **Configurable**: Tune chunk sizes, `k` for retrieval, and models.
* **CLI demo**: Quick interactive loop using **Gemini 1.5 Flash**.


---


## 🧱 Tech Stack


* **LLM & Embeddings**: Google **Gemini API** (via `google-generativeai` / `langchain-google-genai`)
* **Orchestration**: **LangChain**
* **Vector DB**: **Chroma**
* **Python**: 3.10+


---


## 🔎 How it works


1. **Load & split** your Markdown file into overlapping chunks.
2. **Embed** chunks with Gemini API.
3. **Index** embeddings in ChromaDB.
4. **Retrieve** top-k chunks for a query.
5. **Generate** a grounded answer with Gemini using retrieved context.
---
## 🙌 Author

**Achuth Akilesh**  
Product Designer & Data Analyst  
🌐 [Portfolio Website](https://madebyachuth.framer.website/)
