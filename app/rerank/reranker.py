from sentence_transformers import CrossEncoder
from app.config import settings

class Reranker:

    def __init__(self):
        self.model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

    def rerank(self, query, candidates):

        pairs = [(query, doc) for doc in candidates]
        scores = self.model.predict(pairs)

        ranked = sorted(
            zip(candidates, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return [doc for doc, _ in ranked[:settings.RERANK_TOP_K]]