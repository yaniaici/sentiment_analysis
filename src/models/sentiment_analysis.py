from textblob import TextBlob

def analyze_sentiment(text):
    """Analyzes the sentiment of a given text using TextBlob.
    
    Args:
        text (str): The text to analyze.
    
    Returns:
        str: The sentiment of the text ('positive', 'neutral', 'negative').
    """
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

def analyze_tweets(tweets):
    """Applies sentiment analysis to a list of tweets.
    
    Args:
        tweets (list): List of dictionaries containing tweet data.
    
    Returns:
        list: List of dictionaries with the original tweet data and the sentiment analysis results.
    """
    analyzed_tweets = []
    for tweet in tweets:
        sentiment = analyze_sentiment(tweet['text'])
        analyzed_tweets.append({
            'text': tweet['text'],
            'sentiment': sentiment,
            'created_at': tweet['created_at'],
            'user': tweet['user'],
            'retweet_count': tweet['retweet_count'],
            'favorite_count': tweet['favorite_count']
        })
    return analyzed_tweets
