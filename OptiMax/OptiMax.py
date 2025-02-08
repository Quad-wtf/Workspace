import os
import sys
from colorama import Fore, Style
import win32com.client
import editor
import curses
from time import sleep

import editor.editor

# Your ping command
Ping = "ping -l 16 -n 10 google.com"

def execute_command(command):
    """Execute a system command and handle potential errors."""
    try:
        print(f"{Fore.YELLOW}Executing command: {command}{Fore.RESET}")  # Show the command being executed
        exit_code = os.system(command)
        
        if exit_code != 0:
            print(f"{Fore.RED}Error occurred with exit code {exit_code}{Fore.RESET}")
        return exit_code
    except Exception as e:
        print(f"{Fore.RED}Error occurred: {str(e)}{Fore.RESET}")
        return -1

def ipconfig():
    """Handle ipconfig commands like /flushdns and /renew."""
    params = input("Params: /flushdns, /renew: ").strip()

    if params == "/flushdns":
        exit_code = execute_command("ipconfig /flushdns")
    elif params == "/renew":
        print("Renewing IP...")
        exit_code = execute_command("ipconfig /renew")
    else:
        print(f"{Fore.RED}Invalid parameter.{Fore.RESET}")
        return

    if exit_code == 0:
        print(f"{Fore.GREEN}Command executed successfully!{Fore.RESET}")
    else:
        print(f"{Fore.RED}Error occurred with exit code {exit_code}.{Fore.RESET}")

def update():
    """Update external packages using winget and pip."""
    print(f"{Fore.CYAN}Updating external packages...\n{Fore.RESET}")
    
    # Define the commands to run
    commands = [
        "winget upgrade --all --verbose --include-unknown --ignore-security-hash",
        "python.exe -m pip install --upgrade pip",
        "pip-review --local --interactive --continue-on-fail --verbose"
    ]
    
    for command in commands:
        # Execute the command and get the output
        exit_code = execute_command(command)
        
        if exit_code != 0:
            print(f"{Fore.RED}Error occurred with exit code {exit_code}.{Fore.RESET}")
        else:
            print(f"{Fore.GREEN}Successfully executed: {command}{Fore.RESET}")

def create_shortcut(source_exe, destination_path):
    """Create a shortcut using WScript.Shell."""
    try:
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortcut(destination_path)
        shortcut.TargetPath = source_exe
        shortcut.Save()
        print(f"{Fore.LIGHTGREEN_EX}Shortcut created successfully at {destination_path}{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}Error creating shortcut: {str(e)}{Fore.RESET}")

def make_file():
    """Create a new file at the specified location with a given name."""
    filename = input("Enter the name of the file: ").strip()
    save_location = input("Enter the path to save the file (leave empty to save in the current directory): ").strip()

    if not filename:
        print(f"{Fore.RED}File name cannot be empty.{Fore.RESET}")
        return

    if not save_location:
        save_location = os.getcwd()  # Default to the current working directory if no path is provided

    # Create the full path to the file
    file_path = os.path.join(save_location, filename)

    try:
        # Create the file if it doesn't exist
        with open(file_path, 'w') as f:
            print(f"{Fore.LIGHTGREEN_EX}File '{filename}' created successfully at {file_path}{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}Error creating file: {str(e)}{Fore.RESET}")

def rename():
    ren = input("What file would you like to rename? ").strip()
    rename_to = input("What would you like to be the new name? ").strip()

    if not ren:
        print(f"{Fore.RED}File doesn't exist.{Fore.RESET}")
        return
    if not rename_to:
        print(f"{Fore.RED}File name cannot be empty.{Fore.RESET}")
        return
    
    os.system(f"")

def shell():
    """Main shell for executing commands."""
    print(f"{Fore.CYAN}Quality-Of-Life cmdlet. Ver. 4.0\n{Fore.RESET}")
    print(f"{Fore.YELLOW}Available commands: inter, link, update, ipconfig, makefile, edit, content, clear, ?, exit\n{Fore.RESET}")

    while True:
        choice = input(f"{Fore.BLUE}command: {Fore.RESET}").strip().lower()

        if choice == "inter":
            InternetTest()
        elif choice == "link":
            source_exe = input("Enter the path of the executable to create a shortcut for: ")
            destination_path = input("Enter the destination path to save the shortcut: ")
            create_shortcut(source_exe, destination_path)
        elif choice == "exit":
            print(f"{Fore.LIGHTYELLOW_EX}Exiting the shell...{Fore.RESET}")
            break
        elif choice == "update":
            update()
        elif choice == "ipconfig":
            ipconfig()
        elif choice == "makefile":
            make_file()
        elif choice == "edit":
            filename = input("Enter the filename to edit: ").strip()
            print("OptiEditor. Ver. 2.5")
            sleep(0.7)
            curses.wrapper(editor.editor.editor, filename)  # Pass the filename to the editor
        elif choice == "content":
            cat_file()
        elif choice == "clear":
            os.system('cls' if sys.platform == "win32" else 'clear')
        elif choice == "?":
            print("Available commands: inter, link, update, ipconfig, makefile, edit, content, clear, ?, exit")
        else:
            print(f"{Fore.RED}Invalid command. Please try again.{Fore.RESET}")

def cat_file():
    """Display the contents of a specified file."""
    filename = input("What file would you like to see the contents of? ").strip()
    if not filename:
        print(f"{Fore.RED}File name cannot be empty.{Fore.RESET}")
        return

    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"\n{Fore.GREEN}Contents of {filename}: {Fore.RESET}\n")
            print(content)
    except FileNotFoundError:
        print(f"{Fore.RED}Error: The file '{filename}' does not exist.{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Fore.RESET}")

def InternetTest():
    """Test internet connectivity by pinging google."""
    print(f"{Fore.GREEN}Starting internet test...{Fore.MAGENTA}")
    exit_code = execute_command(Ping)
    
    if exit_code == 0:
        print(f"{Fore.LIGHTBLUE_EX}Internet test was successful!{Fore.RESET}")
    else:
        print(f"{Fore.RED}{Style.BRIGHT}Internet test failed with exit code {exit_code}.{Fore.RESET}")

def main():
    shell()

if __name__ == "__main__":
    main()
