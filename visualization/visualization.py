import pandas as pd
import matplotlib.pyplot as plt

from config import CFG
from data_preprocessing import preprocess


def histogram_of_total_goals():
    if not CFG.processed_men_results_path.exists() or not CFG.processed_women_results_path.exists:
        preprocess()

    men_results = pd.read_csv(CFG.processed_men_results_path)
    women_results = pd.read_csv(CFG.processed_women_results_path)

    plt.figure(figsize=(12, 6))
    plt.hist(men_results['total_goals'], alpha=0.5, label='Men')
    plt.hist(women_results['total_goals'], alpha=0.5, label='Women')
    plt.xlabel('Total Goals per Match')
    plt.ylabel('Frequency')
    plt.title('Distribution of Total Goals in FIFA World Cup (Men vs Women)')
    plt.legend()
    plt.show()


def trends_over_time():
    if not CFG.processed_men_results_path.exists() or not CFG.processed_women_results_path.exists:
        preprocess()

    men_results = pd.read_csv(CFG.processed_men_results_path)
    women_results = pd.read_csv(CFG.processed_women_results_path)

    men_results['year'] = pd.to_datetime(men_results['date']).dt.year
    women_results['year'] = pd.to_datetime(women_results['date']).dt.year

    avg_goals_men = men_results.groupby('year')['total_goals'].mean()
    avg_goals_women = women_results.groupby('year')['total_goals'].mean()

    plt.figure(figsize=(12, 6))
    plt.plot(avg_goals_men, label='Men')
    plt.plot(avg_goals_women, label='Women', linestyle='--')
    plt.xlabel('Year')
    plt.ylabel('Average Goals per Match')
    plt.title('Average Goals per Match Over Years (FIFA World Cup)')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # histogram_of_total_goals()
    trends_over_time()
