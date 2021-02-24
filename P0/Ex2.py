import Seq0

FOLDER = './sequences downloaded/'
ID = 'U5'

U5_seq = Seq0.seq_read_fasta(FOLDER + ID)
print('The first 20 bases are:', U5_seq[0:20])