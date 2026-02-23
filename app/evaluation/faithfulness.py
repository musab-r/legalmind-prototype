from deepeval.metrics import FaithfulnessMetric
from deepeval.test_case import LLMTestCase
from app.config import settings

def evaluate_faithfulness(question, answer, context):

    test_case = LLMTestCase(
        input=question,
        actual_output=answer,
        retrieval_context=context
    )

    metric = FaithfulnessMetric(
        threshold=settings.FAITHFULNESS_THRESHOLD
    )

    metric.measure(test_case)

    return metric.score, metric.passed