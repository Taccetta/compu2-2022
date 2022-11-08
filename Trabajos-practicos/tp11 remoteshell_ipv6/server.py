import socketserver as ss
import argparse
import subprocess


def launch():
    argvals = None 
    args = get_args(argvals)
    server(args)

def server(args):

    host = 'localhost'
    port = args.port
    options = {'t': ss.ThreadingTCPServer, 
            'p': ss.ForkingTCPServer}

    with options.get(args.conc)((host, port), TCPRequestHandler) as server:
        print("Online, waiting for connections...")

        try:
            server.serve_forever()
        
        except KeyboardInterrupt:
            print("Shutdown...")
            server.shutdown()

class TCPRequestHandler(ss.BaseRequestHandler):

    def handle(self):
        print(self.client_address, " connected.")
        while True:
            command = self.request.recv(2048).decode("utf-8")
            line_input = ""
            line_input = line_input + subprocess.getoutput(command)
            self.request.send(line_input.encode("utf-8"))


def get_args(argv=None):

    try:
        parser = argparse.ArgumentParser(description='Server Socket')
        parser.add_argument('-p', '--port', type=int, default=0, help="Server port.")
        parser.add_argument('-c', '--conc', required=True, choices=['p', 't'], help="Concurrence type.")
        args = parser.parse_args()

    except:
        print("\nError: Invalid or missing arguments. Try -h to get help.")
        exit(2)

    return parser.parse_args(argv)


class ThreadingTCPServer(ss.ThreadingMixIn, ss.TCPServer):
    pass

class ForkingTCPServer(ss.ForkingMixIn, ss.TCPServer):
    pass

if __name__ == "__main__":
    launch()
