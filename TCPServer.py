# module for networking
import socket

# client-side handling
def main():
    server = socket.socket()
    host = "127.0.0.1" # this computer's IP address
    port = 8000 # arbitrary number to run the server application
    server.bind((host,port)) # allocate host & port to the server
    
    server.listen(1) # allow for 1 connection at a time
    
    client, client_addr = server.accept() # if there's a connection, accept it
    
    # handle the data from the connection
    while True:
        data = client.recv(64).decode('utf-8') # receive 64 byte & decode string
        if not data:
            break
        send_back = data.upper() # upper case the string
        send_back = send_back.encode('utf-8')
        client.send(send_back)
    
    
if __name__ == "__main__":
    main()