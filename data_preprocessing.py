import pandas as pd

from config import CFG


def load_and_preprocess(file_path):
    data = pd.read_csv(file_path)
    data_filtered = data[data['date'] >= '2002-01-01']
    world_cup_data = data_filtered[data_filtered['tournament'] == 'FIFA World Cup']
    world_cup_data['total_goals'] = world_cup_data['home_score'] + world_cup_data['away_score']

    return world_cup_data


def preprocess():
    men_world_cup = load_and_preprocess(CFG.men_results_path)
    women_world_cup = load_and_preprocess(CFG.women_results_path)

    men_world_cup.to_csv(CFG.processed_men_results_path, index=False)
    women_world_cup.to_csv(CFG.processed_women_results_path, index=False)


if __name__ == "__main__":
    preprocess()
