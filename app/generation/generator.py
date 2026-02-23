from openai import OpenAI
from app.generation.prompt import SYSTEM_PROMPT
from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_answer(question, context_chunks):

    context_text = "\n\n".join([str(c) for c in context_chunks])

    response = client.chat.completions.create(
        model=settings.GENERATION_MODEL,
        temperature=0.2,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Context:\n{context_text}\n\nQuestion:\n{question}"
            }
        ]
    )

    return response.choices[0].message.content