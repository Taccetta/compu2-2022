#!/usr/bin/env python
import subprocess as sp
import argparse
from datetime import datetime
import os

def main():

    try:
        parser = argparse.ArgumentParser(description='Shell Command Log Creator')
        parser.add_argument('-c', '--command', help='Shell Command')
        parser.add_argument('-f', '--outfile', help='Output file route')
        parser.add_argument('-l', '--logfile', help='Log file route')
        args = parser.parse_args()

        if args.command == None:
            print("Must specify a Shell Command")
            exit(2)

        if args.outfile == None:
            print("Must specify an output file route")
            exit(2)

        if args.logfile == None:
            print("Must specify an log file route")
            exit(2)

    except:
        print("Error: Invalid Arguments.")
        exit(2)

    scom = sp.Popen(args.command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)
    out, err = scom.communicate()

    print('out: \n\n{0}'.format(out))

    if scom.returncode == 0:
        print('Command : success')
    else:
        errorlog = 1
        print('Error: \n{0}'.format(err))
        print('Command : failed')

    if os.path.isfile(args.logfile + '.txt') == True:
        paramopen = "a"
    else:
        paramopen = "w"

    try:
        textfile = open(args.outfile + ".txt", "w")
        textfile.write('out: \n\n{0}'.format(out))
        textfile.close()
    except:
        print("Error: No such file or directory: '"+ args.outfile +"'")
        exit(2)

    try:
        logfile = open(args.logfile + ".txt", "{0}".format(paramopen))
        today = str(datetime.today())
        if errorlog == 1:
            logfile.write(today + ": Command '" + args.command + "' failed.\n")
        else:
            logfile.write(today + ": Command '" + args.command + "' success.\n")
        logfile.close()
    except:
        print("Error: No such file or directory: '"+ args.logfile +"'")
        exit(2)

if __name__ == "__main__":
    main()