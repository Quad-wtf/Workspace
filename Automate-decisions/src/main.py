from random import choice
from colorama import Fore, Style
import os
import time

def clear_console():
    """Clear the console for Windows or Unix systems."""
    os.system('cls' if os.name == 'nt' else 'clear')

def Randomizer(things):
    """Randomize the list of things and display the result."""
    print(f"{Fore.CYAN}{Style.BRIGHT}Randomizing...")

    things_list = things.split()
    
    if not things_list:
        print(f"{Fore.RED}No items to randomize!")
        return

    print(f"{Fore.GREEN}The answer is... {Fore.YELLOW}{choice(things_list)}{Fore.GREEN}!")

def main():
    clear_console()
    print(f"{Fore.BLUE}Hello! What would you like to randomize?")
    things = input(f"{Fore.YELLOW}~> ").strip()

    if things.lower() == "exit":
        print(f"{Fore.RED}Exiting...")
        return

    Randomizer(things)

if __name__ == "__main__":
    main()

