def validate_citations(answer: str, retrieved_chunks):

    valid_ids = [
        chunk.metadata.get("document_id")
        for chunk in retrieved_chunks
    ]

    for doc_id in valid_ids:
        if doc_id in answer:
            continue

    # Basic validation placeholder
    # Expand with regex-based citation schema validation
    return True