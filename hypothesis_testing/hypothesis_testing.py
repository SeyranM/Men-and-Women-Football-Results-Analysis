import pandas as pd
from loguru import logger
from scipy.stats import ttest_ind

from config import CFG


def load_data(file_path):
    return pd.read_csv(file_path)['total_goals']


def perform_t_test(men_goals, women_goals, significance_level=0.05):
    _, p_val = ttest_ind(men_goals, women_goals)
    result = "reject" if p_val < significance_level else "fail to reject"
    return {"p_val": p_val, "result": result}


def perform_hypothesis_testing():
    men_goals = load_data(CFG.processed_men_results_path)
    women_goals = load_data(CFG.processed_women_results_path)

    result_dict = perform_t_test(men_goals, women_goals)
    return result_dict


if __name__ == "__main__":
    perform_hypothesis_testing()
