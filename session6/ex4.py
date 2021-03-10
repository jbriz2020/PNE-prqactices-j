from P0.Seq0 import Seq
import termcolor

def generate_seqs(pattern, number): # A, 3
    l = []
    for i in range(0, number):
        l.append(Seq(pattern * (i + 1)))
    return l


def print_seqs(list, color):
    for i in range(0, len(list)):
        termcolor.cprint('Sequence ' + str(i) + ': (Length: ' + str(list[i].len()) + ') ' + str(list[i]), color)

seq_list1 = generate_seqs('A', 3)
seq_list2 = generate_seqs('AC', 5)

termcolor.cprint(('List 1:'), 'blue')
print_seqs(seq_list1, 'blue')

print()
termcolor.cprint(('List 2:'), 'green')
print_seqs(seq_list2, 'green')
