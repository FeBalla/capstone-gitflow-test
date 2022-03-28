import pandas as pd


def get_most_retweeted_tweets(data_chunks, n=10):
  '''Gets the N most retweeted tweets and returns a sorted dataframe with the results'''
  top_per_chunk = []

  for chunk in data_chunks:
    top_per_chunk.append(chunk.sort_values("retweetCount", ascending=False).head(n))

  top_retweeted = pd.concat(top_per_chunk).sort_values("retweetCount", ascending=False).head(n)
  return top_retweeted


def display_most_retweeted_tweets(top_data):
  '''Shows the given top of most retweeted tweets showing their content, author and number of 
  retweets'''
  top_pos = 1
  for _, tweet in top_data.iterrows():
    print(f"TOP {top_pos}:")
    print(tweet['content'])
    print(f"> Usuario: {tweet['user']['displayname']} (@{tweet['user']['username']})")
    print(f"> Cantidad de retweets: {tweet['retweetCount']}\n")
    top_pos += 1
