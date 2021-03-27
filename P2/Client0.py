import socket
import termcolor

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self): #te conecta con una pag web
        print('Ok')

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
            print('Server is up')
        except ConnectionRefusedError:
            print('Could not connect to the server. Is it running? Have you checked the Ip and the Port?')

    def __str__(self):
        return 'Connect to SERVER at ' + self.ip + ', PORT: ' + str(self.port)

    def talk(self, msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))
        # Send data.
        print('To server:', msg)
        s.send(msg.encode())
        # Receive data
        response = s.recv(2048).decode('utf-8')
        # Close the socket
        s.close()
        # Return the response
        return 'From server: ' + response

    def debug_talk(self, msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))
        # Send data.
        print('To server:')
        termcolor.cprint(msg, 'blue')
        s.send(msg.encode())
        # Receive data
        response = s.recv(2048).decode('utf-8')
        # Close the socket
        s.close()
        # Return the response
        print('From server:')
        return response




