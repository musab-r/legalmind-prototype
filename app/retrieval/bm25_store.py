from rank_bm25 import BM25Okapi
import numpy as np


class BM25Store:

    def __init__(self, documents: list[str]):
        self.documents = documents
        self.tokenized_docs = [doc.split() for doc in documents]
        self.bm25 = BM25Okapi(self.tokenized_docs)

    def retrieve(self, query: str, top_k: int):
        scores = self.bm25.get_scores(query.split())
        top_indices = np.argsort(scores)[-top_k:]
        return [self.documents[i] for i in top_indices]