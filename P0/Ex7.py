import Seq0

FOLDER = './sequences_downloaded/'
ID = 'U5'

U5_seq = Seq0.seq_read_fasta(FOLDER + ID)
seq = U5_seq[0:20]

print('-------Exercise 7---------')
print('Gene', ID, ':\n' + 'Frag:', seq, '\nComp:', Seq0.seq_complement(seq))