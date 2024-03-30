import os

from loguru import logger

from explanation import explain_results
from hypothesis_testing import perform_hypothesis_testing


def perform_test_and_explain(api_key=os.environ.get("OPENAI_API_KEY")):
    result_dict = perform_hypothesis_testing()
    explanation = explain_results(result_dict, api_key=api_key)

    logger.info("Explanation:")
    logger.info(explanation)


if __name__ == '__main__':
    perform_test_and_explain()
