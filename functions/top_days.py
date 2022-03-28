import pandas as pd


def get_days_with_most_tweets(data_chunks, n=10):
  '''Gets the N days with more tweets and returns a descending sorted dataframe with the results'''
  top_per_chunk = []

  for chunk in data_chunks:
    chunk["date"] = chunk["date"].dt.date

    chunk_count_by_date = chunk["date"].value_counts().sort_index().reset_index()
    chunk_count_by_date.columns = ["date", "tweetsCount"]

    top_per_chunk.append(chunk_count_by_date)

  top_days = pd.concat(top_per_chunk)
  top_days = top_days.groupby("date", as_index=False).sum()
  top_days = top_days.sort_values("tweetsCount", ascending=False).head(n)
  return top_days


def display_days_with_most_tweets(top_data):
  '''Shows the given top of the days with more tweets, showing the date and their number of tweets'''
  top_pos = 1
  for _, day in top_data.iterrows():
    print(f"TOP {top_pos}:")
    print(f"> Fecha: {day['date']}")
    print(f"> Cantidad de tweets: {day['tweetsCount']}\n")
    top_pos += 1
