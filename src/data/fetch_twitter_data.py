import tweepy
import yaml

def load_credentials(config_path):
    """Loads Twitter API credentials from a YAML file."""
    with open(config_path, 'r') as file:
        creds = yaml.safe_load(file)
    return creds

def fetch_data(query, count=100, lang="en"):
    """Fetches tweets using the Twitter API v2 based on a specific query.
    
    Args:
        query (str): The search term to filter tweets.
        count (int): The number of tweets to retrieve.
        lang (str): The language of the tweets.

    Returns:
        list: A list of dictionaries with tweet data.
    """
    # Load credentials from config/credentials.yaml
    credentials = load_credentials("config/credentials.yaml")

    # Authenticate with the Twitter API v2
    client = tweepy.Client(bearer_token=credentials['bearer_token'])

    # Search for tweets using the API v2
    query = f"{query} lang:{lang}"
    tweets = client.search_recent_tweets(query=query, max_results=count, tweet_fields=['created_at', 'text', 'author_id', 'public_metrics'])

    # Process and return the data
    tweets_data = []
    for tweet in tweets.data:
        tweets_data.append({
            "text": tweet.text,
            "created_at": tweet.created_at,
            "user": tweet.author_id,
            "retweet_count": tweet.public_metrics['retweet_count'],
            "favorite_count": tweet.public_metrics['like_count']
        })
    
    return tweets_data

if __name__ == "__main__":
    # Example usage: Fetch 100 tweets containing "python"
    data = fetch_data(query="python", count=100)
    print(f"Retrieved {len(data)} tweets.")
