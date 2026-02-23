import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    EMBEDDING_MODEL = "text-embedding-3-large"
    GENERATION_MODEL = "gpt-4"
    VECTOR_TOP_K = 20
    RERANK_TOP_K = 5
    FAITHFULNESS_THRESHOLD = 0.9

settings = Settings()