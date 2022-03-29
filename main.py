from functions.function_handler import FunctionHandler
import parameters
import time


def display_main_menu():
  '''Shows the main menu with the different available options'''
  print(">> Capstone 2022-1 - Fernando Balladares C.")
  print(f"1. Top {parameters.N_TOP} tweets con más retweets")
  print(f"2. Top {parameters.N_TOP} usuarios con más tweets")
  print(f"3. Top {parameters.N_TOP} días con más tweets")
  print(f"4. Top {parameters.N_TOP} hashtags más usados")
  print(f"{parameters.EXIT_OPTION}. SALIR")


def main():
  '''Main function that runs the program'''
  function_handler = FunctionHandler()
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
  main()
