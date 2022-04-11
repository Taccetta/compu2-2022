#!/usr/bin/
import os
import time
import argparse
from string import ascii_uppercase

def launch():

    print("TP fork_df")
    argvals = None 
    args = get_args(argvals)
    releasethechilds(args.number, args.modverbose, args.route, args.times)
    readresult(args.route)
    exit(0)

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

def releasethechilds(
    num_proc, verbose, route, 
    times):
    if verbose == 1:
        print("Running. Please Wait...\n")

    children_pid = []
    

    flag = False
    for process in range(num_proc):
        pid = os.fork()

        if pid > 0:
            if verbose == 1 and flag is False:
                print("Parent process ID {}".format(os.getpid()))
                flag = True
            children_pid.append(pid)
        
        else:
            if verbose == 1:
                print("Starting child Nº {}, process".format(process+1),"ID {}".format(os.getpid()))
            write_txt(route, times, 
                    process, os.getpid(), 
                    verbose)
            os._exit(os.EX_OK)
    
    for i, proc in enumerate(children_pid):
        codexit = os.waitpid(proc, 0)
        code = os.WEXITSTATUS(codexit[1])
        if verbose == 1:
            print("Child's exit code:", code)

def write_txt(
    route, times, number, 
    cpid, verbose):


    alpha = list(ascii_uppercase)

    if os.path.isfile(route + '.txt') == True:
        paramopen = "a"
    else:
        paramopen = "w"

    try:
        logfile = open(route + ".txt", "{0}".format(paramopen))
        for i in range(times):
            if verbose == 1:
                print("Process {} writing {} letter".format(cpid, alpha[number]))
            logfile.write("{}".format(alpha[number]))
            logfile.flush()
            time.sleep(1)
        logfile.close()
    except:
        print("Error: No such file or directory: '"+ route +"'")
        exit(2)
    
def readresult(route):
    textfile = open(route + ".txt", "r")
    print(textfile.read())
    textfile.flush()
    textfile.close()


if __name__ == "__main__":

    launch()

