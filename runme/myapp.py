import argparse
import os

def printme(name, times):
    """
        Print any string in loop
        params:
            name: Any string/text
            times: How many times to print
    """
    loop = int(times)
    while loop >0:
        print(name)
        loop = loop - 1

if __name__ == "__main__":
    name = input("Enter any string: ")
    loop = input("Enter number of time to print: ") 
    printme(name, loop)
