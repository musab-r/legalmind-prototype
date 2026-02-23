from openai import OpenAI
from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_synthetic_questions(context: str, n: int = 10):

    prompt = f"""
    Generate {n} complex legal multi-hop questions 
    based strictly on the following documents:

    {context}
    """

    response = client.chat.completions.create(
        model=settings.GENERATION_MODEL,
        temperature=0.3,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content