#!/usr/bin/
import os
import argparse
import mmap as m
import sys
import signal as s


class Mayusler():


    def __init__(self):
        self.argvals = None
        self.args = self.get_args(self.argvals)
        self.shared_memory = m.mmap(-1,1024)
        self.son_h1 = 0
        self.son_h2 = 0
        self.textfile = open(self.args.path, 'wb')
        self.parent_pid = os.getpid()
        self.start()


    def signal_call(self):
        s.signal(s.SIGUSR1, self.h1_to_parent_to_h2)


    def h1_to_parent_to_h2(self):
        self.shared_memory.seek(0)
        


    def get_args(
            self, argv=None):
        try:
            parser = argparse.ArgumentParser(description='Childs text inversor')
            parser.add_argument('-f', '--path', required=True, type=str, help='File export route.')
            args = parser.parse_args()

        except:
            print("\nError: Invalid or missing arguments. Must specify a route to save files. Try -h to get help.")
            exit(2)

        return parser.parse_args(argv)
    

    def start(self):
        pass

if __name__ == '__main__':

    iniciating = Mayusler()