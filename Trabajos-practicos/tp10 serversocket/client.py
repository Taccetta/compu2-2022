import socket
import argparse

def launch():
    argvals = None 
    args = get_args(argvals)
    client(args)

def get_args(argv=None):

    try:
        parser = argparse.ArgumentParser(description='Client Server Socket')
        parser.add_argument('-ip', required=True, help="Server IP.")
        parser.add_argument('-p', '--port', required=True, type=int, help="Server port.")
        args = parser.parse_args()

    except:
        print("\nError: Invalid or missing arguments. Try -h to get help.")
        exit(2)

    return parser.parse_args(argv)

def client(args):
    host = args.ip
    port = args.port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        print("Connected!")
        while True:
            command = input("> ")
            message = command.encode('utf-8')
            sock.send(message) 
            print(sock.recv(2048).decode('utf-8'))


if __name__ == '__main__':
    launch()
