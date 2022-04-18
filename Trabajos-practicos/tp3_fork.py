#!/usr/bin/
import os
import time
import argparse
import sys


def releasethechilds(NUM_PROC, verbose):
    children = []
    count = 1
    suma = [NUM_PROC]
    childid = [0 for i in range(NUM_PROC)]
    father = os.getpid()

    for process in range(NUM_PROC):
        pid = os.fork()
        if pid > 0:
            if count == 1:
                if verbose == 1:
                    print("Parent process ID {}".format(os.getpid()), "\n")
            children.append(pid)
            count = 0

        else:
            if verbose == 1:
                print("Starting child Nº {}, process".format(process+1),"ID {}".format(os.getpid()))
            pidc = os.getpid()
            for i in range(0, pidc, 2):
                suma[childid[process]] = suma[childid[process]] + i
                
            if verbose == 1:
                print("Result child Nº {},".format(process+1), "ID {}: ".format(pidc), suma[childid[process]])
                print("Ending child Nº {}, process".format(process+1),"ID {}".format(os.getpid()))
            else:
                print("{} -".format(pidc), father,": ", suma[childid[process]])
            os._exit(0)

    for i, proc in enumerate(children):
        os.waitpid(proc, 0)

    print("\n")
    if verbose == 1:
        text2 = "Parent process is closing..."
        load_animation(text2, 0.01)
    exit(2)

#Lo siguiente es una animacion solo con fines cosmeticos, no tiene relacion con el contenido del TP en sí.
#========================================================================================================
def load_animation(text, t):
    # String to be displayed when the application is loading
    load_str = text
    ls_len = len(load_str)

    # String for creating the rotating line
    animation = "|/-\\"
    #duration
    anicount = counttime = 0
    #pointer       
    i = 0                     
    while (counttime != 100):
        # animation speed
        # smaller the value, faster will be the animation
        time.sleep(t) 
        load_str_list = list(load_str) 
        # x->obtaining the ASCII code
        x = ord(load_str_list[i])
        # y->for storing altered ASCII code
        y = 0                             
        # switch uppercase to lowercase and vice-versa 
        if x != 32 and x != 46:
            if x > 47 and x < 58:
                y = x
                pass           
            elif x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
        # for storing the resultant string
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
        # displaying the resultant string
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
        # Assigning loading string to the resultant string
        load_str = res
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1
    else:
        print("\n")
#========================================================================================================

#Inicio del programa:
if __name__ == "__main__":
    text1 = "Iniciating program"

    try:
        parser = argparse.ArgumentParser(description='Childs processes fork')
        parser.add_argument('-n', '--number', type=int, help='Number of childs')
        parser.add_argument('-v', '--modverbose', help='Verbose Mode', action='count', default=0)
        args = parser.parse_args()

        if args.number == None:
            print("Must specify a number of childs processes")
            exit(2)
        
        if args.modverbose > 1:
            args.modverbose = 1

    except:
        print("\nError: Invalid Arguments. Must specify a number of childs processes")
        exit(2)

    if args.modverbose == 1:
        load_animation(text1, 0.01)

    releasethechilds(args.number, args.modverbose)
