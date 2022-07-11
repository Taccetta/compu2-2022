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


    def start(self):
        print("PID main: ", self.parent_pid)
        self.child_one_start()
        self.child_two_start()


    def child_one_start(self):
        self.signal_config_one()
        self.son_h1 = os.fork()
        if self.son_h1:
            self.textfile.close()
            print("Input line: ")
            for userline in sys.stdin:
                if userline == "bye\n":
                    os.kill(os.getpid(), s.SIGUSR2)
                    break
                self.shared_memory.seek(0)
                self.shared_memory.write(userline.encode())
                os.kill(self.parent_pid, s.SIGUSR1)
                print("Input line: ")
            os._exit(0)


    def notify_h1(self, signum, frame):
        self.shared_memory.seek(0)
        reading = self.shared_memory.readline()
        print("Read: ", reading.decode())


    def notify_h1_parent(self, signum, frame):
        print("Exiting H1 ", self.son_h1)
        os.kill(self.son_h2, s.SIGUSR2)


    def notify_h2(self, signum, frame): 
        self.shared_memory.seek(0)
        reading = self.shared_memory.readline().decode().upper()
        print(reading)
        print("Writing in text file")
        self.textfile.write(reading.encode())
        self.textfile.flush()


    def exit_h2(self, signum, frame):
        print("Exiting H2")
        os._exit(0)


    def signal_config_one(self):
        s.signal(s.SIGUSR1, self.notify_h1)
        s.signal(s.SIGUSR2, self.notify_h1_parent)


    def signal_config_two(self):
        s.signal(s.SIGUSR1, self.notify_h2)
        s.signal(s.SIGUSR2, self.exit_h2)


    def child_two_start(self):
        self.son_h2 = os.fork()
        if self.son_h2:
            self.signal_config_two()
        waiting = True
        if waiting:
            s.pause()



    def get_args(self, argv=None):
        try:
            parser = argparse.ArgumentParser(description='Childs text inversor')
            parser.add_argument('-f', '--path', required=True, type=str, help='File export route.')
            args = parser.parse_args()

        except:
            print("\nError: Invalid or missing arguments. Must specify a route to save files. Try -h to get help.")
            exit(2)

        return parser.parse_args(argv)


if __name__ == '__main__':

    iniciating = Mayusler()