
# LegalMind

Production-grade Modular Retrieval-Augmented Generation (RAG) system designed for high-stakes legal environments requiring strict groundedness, mandatory citation, and automated regression guardrails.



## Overview

LegalMind is a modular knowledge assistant built to query large volumes of internal legal documents (10,000+ contracts, case files, agreements) with:

- High factual accuracy  
- Zero hallucination tolerance  
- Mandatory source attribution  
- Hybrid retrieval (Vector + BM25)  
- Cross-encoder re-ranking  
- CI/CD-enforced evaluation thresholds  

This project operationalizes explainable AI principles for legal-grade reliability.



## Core Architecture

LegalMind follows a modular RAG architecture with six independent layers:

1. Ingestion Layer  
2. Storage Layer  
3. Hybrid Retrieval Layer  
4. Re-ranking Layer  
5. Generation Layer  
6. Evaluation & Guardrails Layer  

Each component is independently replaceable.



## Architecture Flow

### 1. Ingestion

- PDF/DOCX parsing (LlamaIndex)  
- Semantic-aware chunking (~512 tokens, 10% overlap)  
- Metadata enrichment:
  - `document_id`
  - `clause_number`
  - `client_id`
  - `jurisdiction`
  - `effective_date`
- Embedding generation  
- Indexing into:
  - Vector store  
  - BM25 keyword index  

Ingestion runs independently from query-time services.



### 2. Retrieval (Hybrid Search)

Hybrid retrieval combines:

- Semantic similarity (vector search)  
- Keyword precision (BM25)  

Steps:
1. Metadata pre-filtering  
2. Vector similarity search  
3. BM25 search  
4. Merge + deduplicate  
5. Select top 20 candidates  



### 3. Re-ranking

A cross-encoder model re-ranks the top 20 candidates and selects the top 5 most relevant chunks for the LLM context window.

This improves legal clause precision and reduces semantic noise.



### 4. Generation

Strict system prompt enforces:

- Answer only from provided context  
- Mandatory citation of `document_id` and `clause_number`  
- Explicit fallback:  
  `"I don't know based on the available documents."`  
- No speculation  

Temperature ≤ 0.2.



### 5. Evaluation (RAG Triad)

LegalMind integrates automated evaluation directly into CI/CD.

Metrics:

- Faithfulness (Groundedness)  
- Answer Relevance  
- Context Precision  

Build fails automatically if:

- Faithfulness < 0.90  
- Citation validation fails  
- Retrieval precision degrades  



## Agent-Based Validation

Three evaluation agents enforce quality:

### Adversarial Lawyer Agent

Generates synthetic multi-hop legal questions and produces a Golden Dataset for regression testing.

### Compliance Auditor Agent

Extracts claims from responses and verifies each claim against retrieved context to detect hallucinations.

### Shepardizer Agent

Validates:
- Document existence  
- Clause-level references  
- Citation correctness  



## Repository Structure

```

legalmind/
│
├── app/
│   ├── ingestion/
│   ├── retrieval/
│   ├── rerank/
│   ├── generation/
│   ├── evaluation/
│   ├── agents/
│   └── utils/
│
├── tests/
├── docker/
├── .github/workflows/
├── requirements.txt
├── README.md
└── .env.example

````



## Tech Stack

### LLM Layer
- GPT-4 / Claude / Llama 3 (interchangeable)

### Embeddings
- text-embedding-3-large  
- BGE-large  
- E5-large  

### Re-ranking
- Cross-encoder (e.g., `cross-encoder/ms-marco-MiniLM-L-6-v2`)

### Vector Store Options
- Pinecone  
- Weaviate  
- pgvector  
- FAISS  

### Keyword Search
- Elasticsearch / OpenSearch  

### API Layer
- FastAPI  

### Evaluation
- Ragas  
- DeepEval  
- pytest  
- GitHub Actions  

### Caching
- Redis (semantic caching)



## Running Locally

### 1. Install Dependencies

```bash
pip install -r requirements.txt
````

### 2. Set Environment Variables

Create `.env`:

```
OPENAI_API_KEY=your_api_key_here
```

### 3. Run API

```bash
uvicorn app.main:app --reload
```



## Testing

Run evaluation tests:

```bash
pytest
```

CI automatically enforces:

* Faithfulness ≥ 0.90
* Citation integrity
* Retrieval precision



## Design Principles

* Strict modular separation
* Replaceable model components
* Evaluation-first development
* Explainability by default
* CI/CD guardrails
* Production scalability



## Risk Mitigation

| Risk             | Mitigation                                     |
| ---------------- | ---------------------------------------------- |
| Hallucination    | Faithfulness enforcement + Auditor Agent       |
| Broken citations | Shepardizer validation                         |
| Retrieval drift  | Hybrid search + re-ranking + regression tests  |
| Model drift      | Modular LLM abstraction layer                  |
| Scalability      | Metadata filtering + horizontal vector scaling |
| Data privacy     | RBAC + audit logging                           |



## Roadmap

**Phase 1:** Ingestion + Hybrid Retrieval

**Phase 2:** Re-ranking + Strict Generation

**Phase 3:** Evaluation Agents + CI Guardrails

**Phase 4:** Scaling + Caching Optimization

**Phase 5:** Production Governance & Monitoring



## Positioning

LegalMind is not a chatbot layered on legal documents.
It is a rigorously evaluated, modular knowledge infrastructure designed for environments where accuracy, traceability, and auditability are non-negotiable.

## Note

The directory structure has been enhanced beyond the original case study layout to improve modularity, clarity, and service-level separation. This refinement better reflects production-grade architecture practices while remaining fully aligned with the proposed system design.