import tweepy
import yaml

def load_credentials(config_path):
    """Loads Twitter API credentials from a YAML file."""
    with open(config_path, 'r') as file:
        creds = yaml.safe_load(file)
    return creds

def fetch_data(query, count=100, lang="en"):
    """Fetches tweets based on a specific query.
    
    Args:
        query (str): The search term to filter tweets.
        count (int): The number of tweets to retrieve.
        lang (str): The language of the tweets.

    Returns:
        list: A list of dictionaries with tweet data.
    """
    # Load credentials from config/credentials.yaml
    credentials = load_credentials("config/credentials.yaml")

    # Authenticate with the Twitter API
    auth = tweepy.OAuthHandler(credentials['api_key'], credentials['api_secret_key'])
    auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Search for tweets
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang=lang, tweet_mode='extended').items(count)
    
    # Process and return the data
    tweets_data = []
    for tweet in tweets:
        tweets_data.append({
            "text": tweet.full_text,
            "created_at": tweet.created_at,
            "user": tweet.user.screen_name,
            "retweet_count": tweet.retweet_count,
            "favorite_count": tweet.favorite_count
        })
    
    return tweets_data

if __name__ == "__main__":
    # Example usage: Fetch 100 tweets containing "python"
    data = fetch_data(query="python", count=100)
    print(f"Retrieved {len(data)} tweets.")
