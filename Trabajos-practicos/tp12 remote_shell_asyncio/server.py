import socketserver as ss
import argparse
import subprocess
import asyncio


async def launch():
    argvals = None 
    args = get_args(argvals)
    await server(args)

async def server(args):

    host = 'localhost'
    port = args.port

    async with await asyncio.start_server(handle, host, port) as server:
        print("Online, waiting for connections...")

        try:
            await server.serve_forever()
        
        except KeyboardInterrupt:
            print("Shutdown...")
            server.shutdown()



async def handle(reader, writer):
    print("Client connected.")
    while True:
        command = (await reader.read(2048)).decode("utf-8")
        line_input = ""
        line_input = line_input + subprocess.getoutput(command)
        writer.write(line_input.encode("utf-8"))
        await writer.drain()


def get_args(argv=None):

    try:
        parser = argparse.ArgumentParser(description='Server Socket')
        parser.add_argument('-p', '--port', type=int, default=0, help="Server port.")
        args = parser.parse_args()

    except:
        print("\nError: Invalid or missing arguments. Try -h to get help.")
        exit(2)

    return parser.parse_args(argv)



if __name__ == "__main__":
    asyncio.run(launch())
