# Men-and-Women-Football-Results-Analysis

## About the Project

The "Men-and-Women-Football-Results-Analysis" is a Python 3-based hobby project designed for an in-depth analysis and
comparison of football match results from two distinct datasets: men_results.csv and women_results.csv. The project
emphasizes on the statistical aspects of football, particularly focusing on FIFA World Cup matches. A key feature of
this project is the execution of hypothesis testing to compare the average number of goals scored in men's and women's
football matches. Additionally, it employs OPENAI's API to generate intuitive explanations for the results of the
hypothesis testing. To bring the insights to life, the project also includes data visualizations that effectively
showcase the key findings derived from the datasets.

## Technical Requirements

- Python 3
- Additional Python libraries as specified in requirements.txt

## Installation

- Ensure Python 3 is installed on your system.
- Clone or download the repository to your local machine.
- Run pip install -r requirements.txt in the project directory to install necessary Python libraries.

## Usage

The project includes several Python scripts, each serving a distinct purpose in the analysis process:

- config.py: Sets up configuration paths for data and results directories.
- data_preprocessing.py: Handles the loading and preprocessing of the datasets, focusing on World Cup matches and
  calculating total goals per match.
- hypothesis_testing.py: Performs a t-test to compare the average total goals in men's and women's matches, evaluating
  statistical significance.
- explanation.py: Generates explanations for the hypothesis test results using an OpenAI API (requires an API key).
- perform_test_and_explain.py: Integrates hypothesis testing and result explanation, logging the outcome.
- visualization.py: Creates histograms to visualize the distribution of total goals in men's and women's matches.

#### To execute the hypothesis analysis with explanation:

- #### Windows

$Env:OPENAI_API_KEY=your_api_key
python perform_test_and_explain.py

- #### Ubuntu

python perform_test_and_explain.py OPENAI_API_KEY=your_api_key

#### To execute the visualization:

- Execute visualization.py

## Output

The project produces several outputs:

- Preprocessed datasets with a focus on total goals in World Cup matches.
- Results of hypothesis testing, including p-values and decision on the null hypothesis.
- Explanations of the test results (requires OpenAI API key).
- Visualizations of the goal distributions, illustrating differences and similarities between men’s and women’s matches.

## Contributing

I welcome contributions that can improve or expand the project, especially in areas that enhance its value.
Feel free to fork the repository and submit pull requests with your ideas or improvements.

## License

This project is available under an open-source license.

## Contact

For further information, queries, or collaboration proposals, please contact the project
maintainer at seyran.minasyan@gmail.com.
