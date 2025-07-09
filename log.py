import sys

import colorama

from colorama import Fore

__debug = False

def log(message: str, level: int = 1):
    if __debug and level == 0:
        print(Fore.LIGHTBLACK_EX + "DEBUG: " + message + Fore.RESET)
    elif level == 1:
        print(Fore.LIGHTGREEN_EX + "INFO: " + message + Fore.RESET)
    elif level == 2:
        print(Fore.YELLOW + "WARN: " + message + Fore.RESET)
    elif level == 3:
        print(Fore.LIGHTRED_EX + "ERROR: " + message + Fore.RESET)
    elif level == 4:
        print(Fore.RED + "FATAL: " + message + Fore.RESET)
        input("Нажмите Enter чтобы завершить программу\n")
        sys.exit()
