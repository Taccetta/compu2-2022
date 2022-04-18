#!/usr/bin/
import os
import time
import argparse

def launch():

    print("TP fork_df")
    argvals = None 
    args = get_args(argvals)

def get_args(
    argv=None):

    try:
        parser = argparse.ArgumentParser(description='Childs processes fork')
        parser.add_argument('-n', '--number', type=int, help='Number of childs')
        parser.add_argument('-r', '--times', type=int, help='Number of times of write.')
        parser.add_argument('-f', '--route', type=str, help='File export route.')
        parser.add_argument('-v', '--modverbose', help='Verbose Mode', action='count', default=0)
        args = parser.parse_args()

        if args.number == None:
            print("Must specify a number of childs processes")
            exit(2)

        if args.route == None:
            print("Must specify a route to save files.")
            exit(2)

        if args.modverbose > 1:
            args.modverbose = 1

        if args.times == None:
            print("Must specify a number of times")
            exit(2)

    except:
        print("\nError: Invalid or missing arguments. Try -h to get help.")
        exit(2)
        
    return parser.parse_args(argv)

if __name__ == "__main__":

    launch()