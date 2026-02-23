from fastapi import FastAPI
from app.retrieval.hybrid_retriever import HybridRetriever
from app.rerank.reranker import Reranker
from app.generation.generator import generate_answer

app = FastAPI()

retriever = HybridRetriever()
reranker = Reranker()

@app.post("/query")
def query_endpoint(question: str):

    candidates = retriever.retrieve(question)
    top_context = reranker.rerank(question, candidates)
    response = generate_answer(question, top_context)

    return response