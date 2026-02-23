from llama_index.core import VectorStoreIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from app.config import settings


class VectorStore:

    def __init__(self):
        self.embed_model = OpenAIEmbedding(model=settings.EMBEDDING_MODEL)
        self.index = None

    def load_index(self, index):
        self.index = index

    def retrieve(self, query: str, top_k: int):
        retriever = self.index.as_retriever(similarity_top_k=top_k)
        return retriever.retrieve(query)