from Seq1 import Seq
#corregido bien, código imrpoved :)

def print_result(i, sequence):
    print('Sequence ' + str(i) + ': (Length: ' + str(sequence.len()) + ') ' + str(sequence))
    a, c, t, g = sequence.count_bases()
    print('   A: ' + str(a) + ',   C: ' + str(c) + ',   T: ' + str(t) + ',   G: ' + str(g))

print('----- Practice 1, Exercise 5 -----')
s1 = Seq()
s2 = Seq('ACTGA')
s3 = Seq('Invalid seq!')

list_seq = [s1, s2, s3]
for i in range(1, len(list_seq) + 1):
    print_result(i, list_seq[i - 1])