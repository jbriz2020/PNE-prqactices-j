from Client0 import Client
import termcolor

PRACTICE = 2
EXERCISE = 3

print(f"---- Practice {PRACTICE}, Exercise {EXERCISE} ----")

IP = '127.0.0.1'
PORT = 12000
c = Client(IP, PORT)
termcolor.cprint((c.debug_talk('Message 1---')), 'green')
termcolor.cprint((c.debug_talk('Message 2: Testing !!!')), 'green')