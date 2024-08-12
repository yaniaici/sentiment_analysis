from src.data.fetch_twitter_data import fetch_data
from src.data.preprocess import preprocess_data
from src.models.sentiment_analysis import analyze_tweets
from src.visualization.visualize import plot_sentiment_distribution, plot_most_common_words, plot_sentiment_over_time
import yaml

# Load the config file
with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

def main():
    # Step 1: Fetch data
    tweets = fetch_data(
        query=config['twitter']['query'],
        count=config['twitter']['tweet_count'],
        lang=config['twitter']['lang']
    )
    
    # Step 2: Preprocess data
    clean_tweets = preprocess_data(tweets)
    
    # Step 3: Analyze sentiments
    analyzed_tweets = analyze_tweets(clean_tweets)
    
    # Step 4: Visualize results
    plot_sentiment_distribution(analyzed_tweets)
    plot_most_common_words(analyzed_tweets)
    plot_sentiment_over_time(analyzed_tweets)

if __name__ == "__main__":
    main()
