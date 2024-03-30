import os

from loguru import logger
from openai import OpenAI


def explain_results(result_dict, api_key=os.environ.get("OPENAI_API_KEY")):
    if not api_key:
        logger.error(f"You have to provide an OpenAI api key in order to get explanation.")
        logger.error(f"For providing the key you can use the api_key variable of this function or "
                     f"give the key as environment variable with key OPENAI_API_KEY")
        return "Please provide an OpenAI api key..."
    prompt = (f"Explain in simple terms the statistical results: a p-value of "
              f"{result_dict['p_val']} indicating a decision to {result_dict['result']} the null hypothesis.")
    client = OpenAI(
        api_key=api_key
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or another model of your choice
        messages=[
            {"role": "system", "content": "You are a data scientist who helps to understand the hypothesis testing "
                                          "results that were performed on a football dataset. Given the p-value and "
                                          "decision of rejecting the hypothesis or not, you have to explain the "
                                          "results. If you need any additional information for an excellent"
                                          " explanation, provide a list of questions."},
            {"role": "user", "content": prompt}
        ]
    )

    explanation = response.choices[0].message.content

    return explanation
