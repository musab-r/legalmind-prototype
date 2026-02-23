from app.evaluation.faithfulness import evaluate_faithfulness


def audit_response(question, answer, context):

    score, passed = evaluate_faithfulness(question, answer, context)

    if not passed:
        raise ValueError("Hallucination detected")

    return score