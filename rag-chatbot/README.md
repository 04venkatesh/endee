# 🤖 RAG Chatbot using Endee + Ollama (Mistral)

This project demonstrates a production-ready Retrieval-Augmented Generation (RAG) system using vector-based semantic search and a local LLM.

---

## 🚀 Project Overview

This project implements a RAG-based chatbot that allows users to upload PDF documents and interact with them through natural language queries.

The system retrieves relevant context using semantic search over vector embeddings and generates accurate responses using a local LLM (Mistral via Ollama).

---

## ✨ Features

- 📤 Upload and process custom PDF documents  
- 🔍 Semantic search using vector embeddings  
- 🤖 Context-aware question answering (RAG)  
- 💬 Chat-style user interface  
- 🧠 Local LLM (Mistral via Ollama)  
- ⚡ FastAPI backend for scalable API design  
- 🗄️ Endee-ready vector database architecture  

---

## 🧠 Tech Stack

- FastAPI (Backend API)  
- Streamlit (Frontend UI)  
- Sentence Transformers (Embeddings)  
- Ollama + Mistral (Local LLM)  
- Endee (Vector Database - architecture level)  

---

## 🏗️ Architecture

User → Streamlit UI → FastAPI Backend  
→ Embedding Model (Sentence Transformers)  
→ Vector Store (Endee / In-Memory Fallback)  
→ Ollama (Mistral LLM)  
→ Response to User  

---

## 📦 Use of Endee Vector Database

Endee is used as the intended vector database for storing and retrieving embeddings.

### Intended Workflow:
- PDF content is converted into embeddings  
- Embeddings are stored in Endee  
- Semantic search retrieves relevant chunks using vector similarity  
- Retrieved context is passed to the LLM for answer generation  

### Implementation Note:
Endee integration was attempted via REST API endpoints for insertion and search operations.

Due to current endpoint limitations during development, a fallback in-memory vector store is implemented to ensure reliable execution while maintaining compatibility with Endee-based workflows.

The system architecture remains fully compatible with Endee and can be switched to Endee storage once stable endpoints are available.

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd RAG-CHATBOT