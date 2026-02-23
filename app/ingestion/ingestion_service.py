from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.openai import OpenAIEmbedding
from app.config import settings

def ingest_documents(directory_path: str):

    documents = SimpleDirectoryReader(directory_path).load_data()

    splitter = SentenceSplitter(
        chunk_size=512,
        chunk_overlap=50
    )

    nodes = splitter.get_nodes_from_documents(documents)

    embedding_model = OpenAIEmbedding(model=settings.EMBEDDING_MODEL)

    index = VectorStoreIndex(nodes, embed_model=embedding_model)

    index.storage_context.persist()

    return index