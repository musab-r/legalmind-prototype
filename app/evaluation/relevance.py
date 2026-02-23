from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase


def evaluate_relevance(question, answer):

    test_case = LLMTestCase(
        input=question,
        actual_output=answer
    )

    metric = AnswerRelevancyMetric(threshold=0.85)
    metric.measure(test_case)

    return metric.score, metric.passed