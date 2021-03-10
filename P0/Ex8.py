import Seq0

GENE_FOLDER = './sequences downloaded/'
gene_list = ['U5', 'ADA', 'FRAT1', 'FXN']

print('-------Exercise 8---------')
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene)
    print('Gene', gene,': Most frequent base:', (Seq0.most_common_base(Seq0.seq_count(sequence))))
