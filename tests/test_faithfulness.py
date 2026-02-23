from app.evaluation.faithfulness import evaluate_faithfulness

def test_faithfulness_threshold():

    question = "Sample question"
    answer = "Sample answer"
    context = ["Sample context"]

    score, passed = evaluate_faithfulness(question, answer, context)

    assert score >= 0.9
    assert passed