from rank_bm25 import BM25Okapi
import numpy as np
from app.config import settings

class HybridRetriever:

    def __init__(self):
        self.vector_index = None
        self.documents = []

    def retrieve(self, query: str):

        vector_results = self.vector_index.as_retriever(
            similarity_top_k=settings.VECTOR_TOP_K
        ).retrieve(query)

        tokenized_docs = [doc.split() for doc in self.documents]
        bm25 = BM25Okapi(tokenized_docs)
        scores = bm25.get_scores(query.split())

        top_indices = np.argsort(scores)[-settings.VECTOR_TOP_K:]
        keyword_results = [self.documents[i] for i in top_indices]

        combined = list(set(vector_results + keyword_results))

        return combined[:settings.VECTOR_TOP_K]