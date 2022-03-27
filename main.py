from functions.function_handler import FunctionHandler
import pandas as pd
import parameters
import time


def load_data(data_path, chunk_size):
  data_chunks = pd.read_json(data_path, lines=True, chunksize=chunk_size)
  return data_chunks


def display_main_menu():
  print(">> Capstone 2022-1 - Fernando Balladares C.")
  print("1. Top 10 tweets con más retweets")
  print("2. Top 10 usuarios con más tweets")
  print("3. Top 10 días con más tweets")
  print("4. Top 10 hashtags más usados")
  print(f"{parameters.EXIT_OPTION}. SALIR")


def main(data_path):
  data_chunks = load_data(data_path, parameters.DATA_CHUNK_SIZE)
  function_handler = FunctionHandler(data_chunks)

  running = True

  while running:
    time.sleep(parameters.WAITING_TIME)

    display_main_menu()
    option = input("- Selecciona una opción: ")

    if option not in parameters.VALID_OPTIONS:
      print("\033[91mERROR: Ingresa una opción válida\033[0m")
      continue

    if option == parameters.EXIT_OPTION:
      running = False
      continue

    function_handler.use_function(option)

  print("¡Hasta pronto!")


if __name__ == "__main__":
  main(parameters.DATA_PATH)
