from Seq1 import Seq

def print_result(i, sequence):
    print('Sequence ' + str(i) + ': (Length: ' + str(sequence.len()) + ') ' + str(sequence))
    print('Bases: ', sequence.count())
    print('Rev: ', sequence.reverse())
    print('Compl: ', sequence.complement())

print('----- Practice 1, Exercise 8 -----')

s1 = Seq()
s2 = Seq('ACTGA')
s3 = Seq('Invalid seq!')

list_seq = [s1, s2, s3]
for i in range(0, len(list_seq)):
    print_result(i, list_seq[i])


