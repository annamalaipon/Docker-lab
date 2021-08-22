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
    parser = argparse.ArgumentParser(description='Print some string in loop.')
    parser.add_argument('--string', type=str, help='Example Positional Argument')
    parser.add_argument('--time', type=str, help='Example Positional Argument') 
    args = parser.parse_args() 
    printme(args.string, args.time)
