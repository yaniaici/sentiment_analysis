import re
import yaml
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load the config file
with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Load NLTK stopwords
nltk_stopwords = set(stopwords.words('english'))

def clean_tweet(tweet):
    """Cleans the text of a tweet based on the configuration settings.
    
    Args:
        tweet (str): The text of the tweet to be cleaned.
    
    Returns:
        str: The cleaned tweet.
    """
    # Convert to lowercase if specified
    if config['preprocessing']['lowercase']:
        tweet = tweet.lower()
    
    # Remove URLs
    if config['preprocessing']['remove_urls']:
        tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
    
    # Remove mentions
    if config['preprocessing']['remove_mentions']:
        tweet = re.sub(r'@\w+', '', tweet)
    
    # Remove hashtags
    if config['preprocessing']['remove_hashtags']:
        tweet = re.sub(r'#\w+', '', tweet)
    
    # Remove special characters, numbers, and punctuations
    tweet = re.sub(r'\d+', '', tweet)
    tweet = re.sub(r'[^\w\s]', '', tweet)
    
    # Remove stopwords
    if config['preprocessing']['remove_stopwords']:
        tweet = " ".join([word for word in word_tokenize(tweet) if word not in nltk_stopwords])

    return tweet

def preprocess_data(tweets):
    """Applies cleaning to a list of tweets based on the configuration settings.
    
    Args:
        tweets (list): List of dictionaries containing tweet data.
    
    Returns:
        list: List of dictionaries with cleaned tweet text.
    """
    cleaned_tweets = []
    for tweet in tweets:
        cleaned_text = clean_tTweet(tweet['text'])
        cleaned_tweets.append({
            'text': cleaned_text,
            'created_at': tweet['created_at'],
            'user': tweet['user'],
            'retweet_count': tweet['retweet_count'],
            'favorite_count': tweet['favorite_count']
        })
    return cleaned_tweets

if __name__ == "__main__":
    # Example usage with dummy data
    example_tweets = [
        {"text": "Check out the new #Python release! http://python.org @Python", "created_at": "2023-08-10", "user": "user1", "retweet_count": 5, "favorite_count": 10},
        {"text": "I love debugging my code! #coding #developer", "created_at": "2023-08-10", "user": "user2", "retweet_count": 2, "favorite_count": 5},
        {"text": "Follow me for more tech tips! http://techblog.com @TechGuru", "created_at": "2023-08-10", "user": "user3", "retweet_count": 1, "favorite_count": 2}
    ]

    processed_tweets = preprocess_data(example_tweets)
    for tweet in processed_tweets:
        print(f"Cleaned Tweet: {tweet['text']}")
