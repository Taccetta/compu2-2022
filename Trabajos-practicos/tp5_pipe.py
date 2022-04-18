#!/usr/bin/
import os
import argparse
import time

def launch():

    print("TP Pipe")
    argvals = None 
    args = get_args(argvals)
    filetxt = open_file_lines(args.route)
    releasethechilds(filetxt[0], args.route)


def open_file_lines(
    route):
    try:
        with open(route, "r") as filetxt:
            linestext = filetxt.readlines()
            total_lines = len(linestext)
            return linestext, total_lines

    except:
        print("Error: No such file or directory: '"+ route +"'")
        exit(2)


def releasethechilds(
    filetxt, route):

    children_pid = []
    for process in range(len(filetxt)):
        r, w = os.pipe()
        pid = os.fork()
        if pid > 0:
            
            children_pid.append(pid)
            w = os.fdopen(w, "w")
            w.write(filetxt[process])
            w.close()
            

        else:
            print("Starting child Nº {}".format(os.getpid()))
            os.close(w)
            reading = os.fdopen(r)
            wrap = reading.read()[::-1]
            print(wrap)

            r, w = os.pipe()
            w = os.fdopen(w, "w")
            w.write(wrap)
            w.close()
            os._exit(os.EX_OK)

        if pid > 0:
            os.waitpid(children_pid[process], 0)
            reading = os.fdopen(r)
            print("cac", reading.read())
            

    """for i, proc in enumerate(children_pid):
        codexit = os.waitpid(proc, 0)
        code = os.WEXITSTATUS(codexit[1])
        print("Child's exit code:", code)"""


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