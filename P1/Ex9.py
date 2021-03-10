from Seq1 import Seq

def print_result(sequence):
    print('Sequence : (Length: ' + str(sequence.len()) + ') ' + str(sequence))
    print('Bases: ', sequence.count())
    print('Rev: ', sequence.reverse())
    print('Compl: ', sequence.complement())

PROJECT_PATH = '../P0/sequences downloaded/'
print('----- Practice 1, Exercise 9 -----')
s1 = Seq()
s1.read_fasta(PROJECT_PATH + 'ADA')
print_result(s1)



