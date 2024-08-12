# Twitter Sentiment Analysis

### Author: Yani Aici

## Project Overview

This project is a Twitter Sentiment Analysis tool that fetches tweets based on a specified query, preprocesses the data, analyzes the sentiment using TextBlob, and visualizes the results. The tool is built to be flexible and customizable through a configuration file, making it easy to adapt to different needs and queries.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [Acknowledgements](#acknowledgements)

## Features

- Fetch tweets using the Twitter API with customizable query parameters.
- Preprocess tweets by cleaning text, removing stopwords, URLs, mentions, hashtags, and more.
- Analyze sentiment using the TextBlob library.
- Visualize the sentiment distribution, common words, and sentiment trends over time.
- Fully configurable via `config.yaml` for ease of customization.

## Requirements

- Python 3.7+
- The following Python libraries:
  - `tweepy`
  - `textblob`
  - `nltk`
  - `matplotlib`
  - `seaborn`
  - `PyYAML`
  - `wordcloud`
  - `pandas`

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/twitter-sentiment-analysis.git
   cd twitter-sentiment-analysis
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Twitter API Credentials**:
   - Create a `config/credentials.yaml` file with your Twitter API credentials:

     ```yaml
     api_key: "YOUR_API_KEY"
     api_secret_key: "YOUR_API_SECRET_KEY"
     access_token: "YOUR_ACCESS_TOKEN"
     access_token_secret: "YOUR_ACCESS_TOKEN_SECRET"
     ```

5. **Download NLTK Data**:
   - Run the following Python commands to download NLTK stopwords and tokenizer data:

     ```python
     import nltk
     nltk.download('stopwords')
     nltk.download('punkt')
     ```

## Configuration

The project uses a `config.yaml` file located in the `config/` directory for easy configuration. Below is an example configuration:

```yaml
# Twitter API Configuration
twitter:
  query: "python"
  tweet_count: 100
  lang: "en"
  result_type: "recent"
  fetch_mode: "extended"

# Preprocessing Configuration
preprocessing:
  remove_stopwords: true
  lowercase: true
  remove_urls: true
  remove_mentions: true
  remove_hashtags: true
  remove_numbers: true
  remove_special_characters: true

# Sentiment Analysis Configuration
sentiment_analysis:
  method: "textblob"
  positive_threshold: 0.1
  negative_threshold: -0.1

# Visualization Configuration
visualization:
  sentiment_distribution:
    plot_type: "bar"
    color_palette: "viridis"
  common_words:
    top_n: 10
  sentiment_over_time:
    time_interval: "D"

# Data Storage Paths
data_paths:
  raw_data: "data/raw/"
  processed_data: "data/processed/"
  external_data: "data/external/"

# Logging Configuration
logging:
  level: "INFO"
  file: "logs/project.log"
```

## Usage

1. **Run the Main Script**:
   - The main script integrates all components of the project. To run the complete sentiment analysis pipeline, use:

   ```bash
   python main.py
   ```

2. **Explore with Jupyter Notebooks**:
   - Alternatively, you can explore and analyze the data using the provided Jupyter notebooks in the `notebooks/` directory.

## Project Structure

```plaintext
twitter-sentiment-analysis/
│
├── config/
│   ├── config.yaml          # Configuration file
│   └── credentials.yaml     # Twitter API credentials (not included in version control)
│
├── data/
│   ├── raw/                 # Raw data fetched from Twitter
│   ├── processed/           # Cleaned and preprocessed data
│   └── external/            # External datasets (optional)
│
├── notebooks/               # Jupyter notebooks for exploration and analysis
│   ├── 01-data-exploration.ipynb
│   ├── 02-preprocessing.ipynb
│   ├── 03-modeling.ipynb
│   └── 04-visualization.ipynb
│
├── src/
│   ├── data/
│   │   ├── fetch_twitter_data.py  # Fetch tweets from Twitter
│   │   ├── preprocess.py          # Preprocess tweet data
│   │   └── __init__.py
│   │
│   ├── models/
│   │   ├── sentiment_analysis.py  # Analyze sentiment of tweets
│   │   └── __init__.py
│   │
│   ├── visualization/
│   │   ├── visualize.py           # Visualize sentiment analysis results
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── logs/                   # Directory for log files
│   └── project.log
│
├── .gitignore              # Git ignore file to exclude sensitive and unnecessary files
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── main.py                 # Main script to run the project
```

## Acknowledgements

- This project was developed by **Yani Aici** as a hands-on learning experience in Twitter sentiment analysis and Python programming.
- The project uses the [TextBlob](https://textblob.readthedocs.io/en/dev/) library for sentiment analysis and [Tweepy](https://www.tweepy.org/) for accessing the Twitter API.
- Special thanks to the open-source community for providing the tools and libraries used in this project.