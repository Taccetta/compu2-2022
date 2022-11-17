import argparse
from celery import Celery
import math

app = Celery("operations",
            broker="redis://localhost",
            backend="redis://localhost:6379")


def get_args(argv=None):

    try:
        parser = argparse.ArgumentParser(description='Celery Matrix Calc')
        parser.add_argument('-f', '--file',  required=True,
                            help='txt path file.')
        parser.add_argument('-c', '--calc', type=str, required=True,
                            help="Operation set.")
        args = parser.parse_args()

    except:
        print("\nError: Invalid or missing arguments. Try -h to get help.")
        exit(2)

    return parser.parse_args(argv)


def main(args):
    
    matrix = []

    with open(args.file, 'r') as file:

        for line in file.readlines():
            row = line.strip("\n ").split(', ')
            for number in row:
                matrix.append(float(number))


    if args.calc == 'raiz':
        newmatrix = raiz.delay(matrix)
    elif args.calc == 'pot':
        newmatrix = pot.delay(matrix)
    elif args.calc == 'log':
        newmatrix = log.delay(matrix)

    
    i = 0
    for number in newmatrix.get():
        print(str(number) + ", ", end="")
        i += 1
        if i == 3:
            print("\n", end="")


@app.task
def raiz(matrix):
    i = 0
    for number in matrix:
        result = math.sqrt(number)
        matrix[i] = result
        i += 1
    return matrix


@app.task
def pot(matrix):
    i = 0
    for number in matrix:
        result = number ** 2
        matrix[i] = result
        i += 1
    return matrix


@app.task
def log(matrix):
    i = 0
    for number in matrix:
        result = math.log10(number)
        matrix[i] = result
        i += 1
    return matrix


if __name__ == '__main__':
    main(get_args())
