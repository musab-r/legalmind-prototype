def evaluate_context_precision(retrieved_chunks, expected_chunk_ids):

    retrieved_ids = [
        chunk.metadata.get("document_id")
        for chunk in retrieved_chunks
    ]

    hits = sum(1 for doc_id in expected_chunk_ids if doc_id in retrieved_ids)

    precision = hits / len(expected_chunk_ids) if expected_chunk_ids else 0

    return precision, precision > 0