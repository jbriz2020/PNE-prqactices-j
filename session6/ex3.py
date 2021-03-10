from P0.Seq0 import Seq

def generate_seqs(pattern, number): # A, 3
    l = []
    for i in range(0, number):
        l.append(Seq(pattern * (i + 1)))
    return l

def print_seqs(list):
    for i in range(0, len(list)):
        print('Sequence', i, ': (Length: ', list[i].len(), ')', list[i])

seq_list1 = generate_seqs('A', 3)
seq_list2 = generate_seqs('AC', 5)

print('List 1:')
print_seqs(seq_list1)

print()
print('List 2:')
print_seqs(seq_list2)
