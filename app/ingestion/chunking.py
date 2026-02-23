from llama_index.core.node_parser import SentenceSplitter


def get_chunker(chunk_size: int = 512, overlap: int = 50):
    return SentenceSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )