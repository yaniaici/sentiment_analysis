import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_tweet(tweet):
    tweet = re.sub(r'http\S+', '', tweet)  # No URLs
    tweet = re.sub(r'@\w+', '', tweet)  # No mentions
    tweet = re.sub(r'#', '', tweet)  # No hashtags
    tweet = re.sub(r'RT[\s]+', '', tweet)  # No "RT"
    tweet = re.sub(r'\W', ' ', tweet)  # No special characters
    tweet = tweet.lower()  # Convert to lowercase
    tweet = ' '.join([word for word in tweet.split() if word not in stop_words])
    return tweet