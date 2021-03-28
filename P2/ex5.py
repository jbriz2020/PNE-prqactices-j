from Client0 import Client
from pathlib import Path

PRACTICE = 2
EXERCISE = 5

print(f"---- Practice {PRACTICE}, Exercise {EXERCISE} ----")

IP = '127.0.0.1'
PORT = 12000
c = Client(IP, PORT)
(c.debug_talk('Sending U5 gene to server...'))
(c.debug_talk(Path('./sequences downloaded/U5').read_text()))
