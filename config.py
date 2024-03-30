from pathlib import Path


class CFG:

    parent_dir = Path(__file__).parent
    data_dir = parent_dir.joinpath("data")
    raw_data_dir = data_dir.joinpath("raw_data")
    processed_data = data_dir.joinpath("processed_data")
    results_dir = data_dir.joinpath("results")

    men_results_path = raw_data_dir.joinpath("men_results.csv")
    women_results_path = raw_data_dir.joinpath("women_results.csv")
    processed_men_results_path = processed_data.joinpath("men_world_cup_processed.csv")
    processed_women_results_path = processed_data.joinpath("women_world_cup_processed.csv")
