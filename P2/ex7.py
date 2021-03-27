import termcolor
import colorama
from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7

print(f"---- Practice {PRACTICE}, Exercise {EXERCISE} ----")
IP = "127.0.0.1"
PORT = 12000
PORT2 = 12700
c = Client(IP, PORT) #conn to server1
c2 = Client(IP, PORT2) #conn to server2

s = Seq()
s.read_fasta('./sequences downloaded/U5')

count = 0
i = 0
while i < len(s.strbases) and count < 10:
    colorama.init(strip='False')
    fragment = s.strbases[i: i+10]
    count += 1
    i += 10
    print('Fragment', count, ':', fragment)
    if count % 2 == 0:
        print(c2.talk('Fragment' + str(count) + ': ' + termcolor.colored(fragment, 'green')))
    else:
        print(c.talk('Fragment' + str(count) + ': ' + termcolor.colored(fragment, 'green')))