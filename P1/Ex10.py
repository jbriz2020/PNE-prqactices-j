from Seq1 import Seq

PROJECT_PATH = '../P0/sequences downloaded/'
gene_list = ['U5', 'ADA', 'FRAT1', 'FXN']

print('----- Practice 1, Exercise 10 -----')

for gene in gene_list:
    sequence = Seq()
    sequence.read_fasta(PROJECT_PATH + gene)
    print('Gene', gene,': Most frequent base:', (Seq.most_common_base(Seq.count(sequence))))
