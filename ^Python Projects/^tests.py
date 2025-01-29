import os
import sys
from memory_profiler import *
import time
import keyboard

@profile
def get_memory(list_size):
    list = ['hello'] * list_size

os.system("@echo off")

options = print("What would you like to test?\n1. Internet \n2. Memory \n3. CPU")
val = input("=> ") 
def ping_test():
        if val == '1':
            print("Testing internet speed... (press 'CTRL + C' to stop the test)")
            os.system("ping google.com -t")
            if KeyboardInterrupt:
                 while True:
                    print("Internet test cancelled.")
                    sys.exit(0)
ping_test()
    
def mem_test():             
    if val == '2':
        list_size = int(input("Enter the size of the list: "))
        print("Testing memory usage with a list of size...", list_size)
        get_memory(list_size)
if val == '3':
    pass

