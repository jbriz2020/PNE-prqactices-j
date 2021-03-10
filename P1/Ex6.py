from Seq1 import Seq

def print_result(i, sequence):
    print('Sequence ' + str(i) + ': (Length: ' + str(sequence.len()) + ') ' + str(sequence))
    print('Bases: ', sequence.count())

s1 = Seq()
s2 = Seq('ACTGA')
s3 = Seq('Invalid seq!')

print('----- Practice 1, Exercise 6 -----')

list_seq = [s1, s2, s3]
for i in range(0, len(list_seq)):
    print_result(i, list_seq[i])
