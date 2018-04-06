''' Client-side '''

import socket
import argparse

def main():
    host = '127.0.0.1'
    port = 8000 # the port of the server

    s = socket.socket()
    s.connect((host, port)) # connect to the server
    parser = argparse.ArgumentParser()
    parser.add_argument("message", help = "Message to be sent to the server"\
    , type = str )

    args = parser.parse_args()
    print("Message: ", args.message)
    s.send(args.message.encode('utf-8'))
    data = s.recv(64).decode('utf-8')
    print("Received from server: " + data)


if __name__ == "__main__":
    main()
