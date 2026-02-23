import uuid
from datetime import datetime


def enrich_metadata(node, source_type="contract"):
    node.metadata.update({
        "document_id": str(uuid.uuid4()),
        "source_type": source_type,
        "ingested_at": datetime.utcnow().isoformat()
    })
    return node