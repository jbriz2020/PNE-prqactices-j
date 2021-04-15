# We create the socket, bind it to its IP and PORT parameters and configure it for being a listening socket. Finally we close the socket.

import socket

PORT = 8080
IP = "localhost" #you can also use ur laptop's IP or 120.0.0.1

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
# ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

# -- Waits for a client to connect
print("Waiting for Clients to connect")
ls.accept()

print("A client has connected to the server!")

# -- Close the socket
ls.close()
