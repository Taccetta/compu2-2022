#!/usr/bin/
import argparse
from itertools import count
import math
import sys
import multiprocessing as mp


def start():
    read_matrix()
    processing(numbers)


def calculation(number):
    global count


    for num in number:
        if args.calculus == "raiz":
            print(round(math.sqrt(int(num[:1]))), end = ", ")

        if args.calculus == "pot":
            print(round(int(num[:1]) ** 2), end = ", ")

        if args.calculus == "log":
            print(round(math.log10(int(num[:1]))), end = ", ")

    count += 1
    if count == 3:
        print("\n")


def processing(matrix):
    
    with mp.Pool(int(args.num_process)) as p:
        for element in matrix:
            p.map(calculation,element)


def read_matrix():
    for line in textfile.readlines():
        row = line.strip("\n ").split(', ')
        numbers.append(row)


def get_args(argv=None):
    try:
        parser = argparse.ArgumentParser(description='Childs text inversor')
        parser.add_argument('-f', '--path', required=True, type=str, help='File export route.')
        parser.add_argument('-p', '--num_process', required=True, type=int, help='Number of Processes.')
        parser.add_argument('-c', '--calculus', required=True, type=str, help='Calculus Function.')
        args = parser.parse_args()

    except:
        print("\nError: Invalid or missing arguments. Try again.")
        exit(2)

    return parser.parse_args(argv)


if __name__ == '__main__':

    argvals = None
    args = get_args(argvals)
    textfile = open(args.path, 'r')
    filetxt = 0
    numbers = []
    result = 0
    count = 0
    start()
