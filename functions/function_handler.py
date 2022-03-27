from functions.top_retweets import get_most_retweeted_tweets
from functions.top_users import get_users_with_most_tweets
from functions.top_days import get_days_with_most_tweets
from functions.top_hashtags import get_most_used_hasthags


class FunctionHandler:
  def __init__(self, data) -> None:
      self.data = data

  def use_function(self, option) -> str:
    if option == "1":
      response = get_most_retweeted_tweets(self.data)
    
    if option == "2":
      response = get_users_with_most_tweets(self.data)

    if option == "3":
      response = get_days_with_most_tweets(self.data)

    if option == "4":
      response = get_most_used_hasthags(self.data)

    return response
