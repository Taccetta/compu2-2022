#!/usr/bin/
import os
import time
import argparse

def launch():

    print("TP Pipe")
    argvals = None 
    args = get_args(argvals)
    filetxt = open_file(args.route)
    print(filetxt[0])

def open_file(
    route):
    try:
        with open(route, "r") as filetxt:
            linestext = filetxt.readlines()
            total_lines = len(linestext)
            return linestext, total_lines
    except:
        print("Error: No such file or directory: '"+ route +"'")
        exit(2)

def reading_lines(
    filetxt):
    print(filetxt.readlines())

def releasethechilds(
    route):

    children_pid = []

def invert_chain(
    chain):
    return chain[::-1]

def get_args(
    argv=None):

    try:
        parser = argparse.ArgumentParser(description='Childs text inversor')
        parser.add_argument('-f', '--route', type=str, help='File export route.')
        args = parser.parse_args()

    except:
        print("\nError: Invalid or missing arguments. Must specify a route to save files. Try -h to get help.")
        exit(2)

    return parser.parse_args(argv)

if __name__ == "__main__":

    launch()