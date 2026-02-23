from app.retrieval.hybrid_retriever import HybridRetriever
from app.rerank.reranker import Reranker


def get_retriever():
    return HybridRetriever()


def get_reranker():
    return Reranker()