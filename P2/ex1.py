from Client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f"---- Practice {PRACTICE}, Exercise {EXERCISE} ----")

IP = '127.0.0.1'
PORT = 8080
c = Client(IP, PORT)
#c.advanced_ping()
c.ping()
print(f'IP: {c.ip}, Port: {c.port}')