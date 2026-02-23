import hashlib
import redis
import json


class SemanticCache:

    def __init__(self, host="localhost", port=6379):
        self.client = redis.Redis(host=host, port=port)

    def _hash(self, query_embedding):
        return hashlib.sha256(
            str(query_embedding).encode()
        ).hexdigest()

    def get(self, query_embedding):
        key = self._hash(query_embedding)
        result = self.client.get(key)
        return json.loads(result) if result else None

    def set(self, query_embedding, response):
        key = self._hash(query_embedding)
        self.client.set(key, json.dumps(response))