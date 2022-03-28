import pandas as pd


def get_users_with_more_tweets(data_chunks, n=10):
  '''Gets the N users with more tweets and returns a descending sorted dataframe with the results'''
  top_per_chunk = []

  for chunk in data_chunks:
    chunk["displayname"] = chunk["user"].apply(lambda user: user.get("displayname"))
    chunk["username"] = chunk["user"].apply(lambda user: user.get("username"))

    chunk_count_by_user =  chunk.groupby(["username", "displayname"])
    chunk_count_by_user = chunk_count_by_user.size().reset_index().rename(columns={0:'tweetsCount'})
    
    top_per_chunk.append(chunk_count_by_user)

  top_users = pd.concat(top_per_chunk)
  top_users = top_users.groupby(["username", "displayname"], as_index=False).sum()
  top_users = top_users.sort_values("tweetsCount", ascending=False).head(n)
  return top_users


def display_users_with_more_tweets(top_data):
  '''Shows the given top of the users with more tweets, showing their username, displayname and  
  number of tweets'''
  top_pos = 1
  for _, user in top_data.iterrows():
    print(f"TOP {top_pos}:")
    print(f"> Usuario: {user['displayname']} (@{user['username']})")
    print(f"> Cantidad de tweets: {user['tweetsCount']}\n")
    top_pos += 1
