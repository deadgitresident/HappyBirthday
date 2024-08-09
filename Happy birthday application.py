#!/usr/bin/python
# << CODE BY KAZELEGENDO

# IMPORT MODULE

import os
import time
import sys

Bl = '\033[30m'  # VARIABLE 
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'

def run_banner():
    clear()
    time.sleep(1)
    sys.stderr.write(f"""{Wh}
        {Wh}--------------------------------
        {Wh}| {Gr}BIRTHDAY SURPRISE FOR YOU {Wh}|
        {Wh}|       {Gr}@CODE BY KAZELEGENDO      {Wh}|
        {Wh}--------------------------------
   
        """)

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux
    else:
        _ = os.system('clear')

def print_typing(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

def main():
    clear()
    run_banner()
    print(f"{Wh}\nHello, we have a surprise for you, do you want to see it? {Gr}")
    response = input(f"{Wh}Enter 'Yes' or 'No': {Gr}").lower()

    if response == 'yes':
        print_typing(" **Happy Birthday !** ")
    elif response == 'no':
        print_typing(" **Are you sure?** ")
        response2 = input(f"{Wh}Enter 'Yes' or 'No': {Gr}").lower()
        if response2 == 'yes':
            print(f"{Wh}Sorry, you might miss the surprise but I understand.{Gr}")
        else:
            print_typing(" **Happy Birthday !** ")
    else:
        print(f"{Re}Invalid response. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()