import socket
'''Server-side'''
def main():
    host = '127.0.0.1' # default for current computer
    port = 8000
    ser = socket.socket()
    ser.bind((host, port))
    print("Binding successful")


    ser.listen(1) # listen to one connection at the time
    client, client_addr = ser.accept()
    print("Connection from ", client, " with addr ", client_addr)

    while True:
        print("Enter while loop ")
        # receive 64 byte at the time & decode by utf-8 (used for string)
        data = client.recv(64).decode('utf-8')
        if not data:
            break
        data = data.upper() # convert data string to upper case
        send_back = data.encode('utf-8')
        client.send(send_back)
    print("Out of program ")
    client.close() # close the connection

if __name__ == "__main__":
    main()
