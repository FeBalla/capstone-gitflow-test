import pandas as pd
import numpy as np


def extract_hashtags(text):
  '''Returns a list of hashtags inside of the given text removing duplicateds'''
  non_duplicated = set(part[1:] for part in text.split() if part.startswith("#") and part != "")
  return list(non_duplicated)


def get_most_used_hasthags(data_chunks, n=10):
  '''Gets the N most used hashtags and returns a descending sorted dataframe with the results'''
  top_per_chunk = []

  for chunk in data_chunks:
    chunk["hashtags"] = chunk["content"].apply(lambda content: extract_hashtags(content))

    chunk_hashtags = np.array(chunk.hashtags.sum())
    hashtags, tweetsCount = np.unique(chunk_hashtags, return_counts=True)

    top_per_chunk.append(np.asarray((hashtags, tweetsCount)).T)

  top_hashtags = pd.DataFrame(np.concatenate(top_per_chunk), columns=["hashtag", "tweetsCount"])
  top_hashtags["tweetsCount"] = pd.to_numeric(top_hashtags["tweetsCount"])
  top_hashtags = top_hashtags.groupby("hashtag", as_index=False).sum()
  top_hashtags = top_hashtags.sort_values("tweetsCount", ascending=False).head(n)
  
  return top_hashtags


def display_most_used_hasthags(top_data):
  '''Shows the given top of the most used hashtags, showing their name and number of tweets'''
  top_pos = 1
  for _, hashtag in top_data.iterrows():
    print(f"TOP {top_pos}:")
    print(f"> Hashtag: #{hashtag['hashtag']}")
    print(f"> Cantidad de tweets: {hashtag['tweetsCount']}\n")
    top_pos += 1
