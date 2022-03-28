import pandas as pd


def load_data(data_path, chunk_size):
  '''Loads and the JSON tweets data in data_path in chunks of an specific size'''
  data_chunks = pd.read_json(data_path, lines=True, chunksize=chunk_size)
  return data_chunks
