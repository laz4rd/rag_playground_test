# RAG Playground

A private experimentation repository for building and understanding the core AI pipeline behind the Kaju Open Source study platform.

This repository serves as a sandbox for researching, testing, and validating Retrieval-Augmented Generation (RAG) concepts before integrating them into the larger Kaju ecosystem.

---

## Purpose

The goal of this project is to learn and prototype the complete local AI workflow required for an AI-powered study assistant:

```text
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Database
 ↓
Semantic Retrieval
 ↓
Local LLM
 ↓
Answer Generation
```

Everything in this repository is focused on understanding how documents can be transformed into searchable knowledge using local AI models.

---

## Current Features

### PDF Processing
- Extract text from PDF documents
- Basic preprocessing and cleaning

### Chunking
- Split large documents into manageable chunks
- Context-preserving chunk overlap

### Embeddings
- Local embedding generation using Ollama
- Semantic vector creation for document chunks

### Vector Database
- ChromaDB integration
- Persistent vector storage
- Metadata support

### Semantic Search
- Query embedding generation
- Similarity-based retrieval
- Top-K relevant chunk retrieval

### Retrieval-Augmented Generation (RAG)
- Local LLM integration via Ollama
- Context-aware question answering
- Document-grounded responses

---

## Tech Stack

### AI Models
- Ollama
- Qwen
- Nomic Embed

### AI Components
- Retrieval-Augmented Generation (RAG)
- Embeddings
- Semantic Search

### Storage
- ChromaDB

### Language
- Python

---

## Repository Structure

```text
rag_playground/
│
├── documents/
│   └── sample.pdf
│
├── chroma_db/
│
├── pdf_processor.py
├── chunker.py
├── embedder.py
├── ingest.py
├── search.py
├── rag_chat.py
│
├── requirements.txt
└── README.md
```

---

## Learning Objectives

This repository explores:

- PDF ingestion pipelines
- Intelligent chunking strategies
- Embedding generation
- Vector databases
- Semantic retrieval
- Context assembly
- Prompt engineering
- Local LLM integration
- End-to-end RAG systems

---

## Future Work

Potential experiments include:

- Advanced chunking techniques
- Hybrid search
- Retrieval evaluation
- Multi-document retrieval
- Citation-aware responses
- Automatic note generation
- Summary generation
- Flashcard generation
- Knowledge graph experiments

---

## Relation to Kaju Open Source

This repository is an internal research and development playground used to prototype the AI stack that will eventually power Kaju Open Source.

Kaju's long-term goal is to transform academic resources into a shared, searchable, AI-powered knowledge repository for students.

This repository exists solely to validate the underlying AI and RAG architecture before integration into the main platform.

---

## Status

🚧 Experimental / Research Repository

Actively used for learning, benchmarking, and prototyping local AI workflows.
