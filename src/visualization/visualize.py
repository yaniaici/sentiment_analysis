import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from collections import Counter
from wordcloud import WordCloud

def plot_sentiment_distribution(analyzed_tweets):
    """Plot the distribution of sentiments.

    Args:
        analyzed_tweets (list): List of dictionaries containing tweets and their sentiment labels.
    """
    # Convert the list of analyzed tweets into a DataFrame for easier plotting
    df = pd.DataFrame(analyzed_tweets)
    
    # Count the number of each sentiment
    sentiment_counts = df['sentiment'].value_counts()
    
    # Plotting the distribution of sentiments
    plt.figure(figsize=(8, 6))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette='viridis')
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Tweets')
    plt.show()

def plot_most_common_words(analyzed_tweets, sentiment=None, top_n=10):
    """Plot the most common words for a given sentiment or overall.

    Args:
        analyzed_tweets (list): List of dictionaries containing tweets and their sentiment labels.
        sentiment (str): Sentiment to filter by (optional). If None, plots overall most common words.
        top_n (int): Number of top words to plot.
    """
    
    # Filter tweets by sentiment if specified
    if sentiment:
        tweets = [tweet['text'] for tweet in analyzed_tweets if tweet['sentiment'] == sentiment]
    else:
        tweets = [tweet['text'] for tweet in analyzed_tweets]
    
    # Tokenize the words
    words = " ".join(tweets).split()
    common_words = Counter(words).most_common(top_n)
    
    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, max_words=top_n, background_color='white').generate(" ".join(words))
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Most Common Words{" for " + sentiment if sentiment else ""}')
    plt.show()

def plot_sentiment_over_time(analyzed_tweets):
    """Plot the sentiment over time.

    Args:
        analyzed_tweets (list): List of dictionaries containing tweets and their sentiment labels.
    """
    # Convert the list of analyzed tweets into a DataFrame
    df = pd.DataFrame(analyzed_tweets)
    
    # Convert 'created_at' to datetime if it isn't already
    df['created_at'] = pd.to_datetime(df['created_at'])
    
    # Group by date and sentiment, then count occurrences
    sentiment_over_time = df.groupby([df['created_at'].dt.date, 'sentiment']).size().unstack().fillna(0)
    
    # Plotting the sentiment over time
    sentiment_over_time.plot(kind='line', figsize=(12, 6))
    plt.title('Sentiment Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Tweets')
    plt.show()
