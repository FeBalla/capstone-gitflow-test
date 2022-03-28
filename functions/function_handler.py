from functions.top_retweets import get_most_retweeted_tweets, display_most_retweeted_tweets
from functions.top_users import get_users_with_more_tweets, display_users_with_more_tweets
from functions.top_days import get_days_with_more_tweets, display_days_with_more_tweets
from functions.top_hashtags import get_most_used_hasthags, display_most_used_hasthags
from functions.utils import load_data
import parameters


class FunctionHandler:
  def __init__(self) -> None:

    self.functions = {
      "1": [get_most_retweeted_tweets, display_most_retweeted_tweets],
      "2": [get_users_with_more_tweets, display_users_with_more_tweets],
      "3": [get_days_with_more_tweets, display_days_with_more_tweets],
      "4": [get_most_used_hasthags, display_most_used_hasthags],
    }

    self.saved_responses = {
      "1": None,
      "2": None,
      "3": None,
      "4": None,
    }

  def use_function(self, option) -> str:
    '''Uses a function according to the given option (assumes is valid) and displays the response. 
    Saves the results to improve the performance for repeated requests'''
    display_function = self.functions[option][1]

    if self.saved_responses[option] is None:
      data_chunks = load_data(parameters.DATA_PATH, parameters.DATA_CHUNK_SIZE)

      selected_function = self.functions[option][0]
      self.saved_responses[option] = selected_function(data_chunks, parameters.N_TOP)

    display_function(self.saved_responses[option])
