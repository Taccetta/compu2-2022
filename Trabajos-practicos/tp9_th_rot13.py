
import sys
import multiprocessing as mp
import threading
import codecs

class Cypher13():

    def __init__(self):
        self.q = mp.Queue()
        self.r, self.e = mp.Pipe()
        self.child1 = 0
        self.child2 = 0
        self.start()


    def start(self):
        self.child1 = threading.Thread(target=self.stinput, args=(self.q, self.r))
        self.child2 = threading.Thread(target=self.rot_13_cypher, args=(self.q, self.e))

        self.child1.start()
        self.child2.start()

        self.child1.join()
        self.child2.join()


    def stinput(self, queue, pipe):
        sys.stdin = open(0)
        print("Input line: ")
        for line in sys.stdin:
            print(line)
            pipe.send(line)
            print('Encode: ', queue.get())
            print("Input line: ")
        pipe.close()


    def rot_13_cypher(self, queue, pipe):
        while True:
            msg = pipe.recv()
            queue.put(codecs.encode(msg, 'rot13'))


if __name__ ==  '__main__':

    starting = Cypher13()