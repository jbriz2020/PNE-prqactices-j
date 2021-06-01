import Seq0

GENE_FOLDER = './sequences_downloaded/'
gene_list = ['U5', 'ADA', 'FRAT1', 'FXN']

print('-------Exercise3---------')
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene)
    print('Gene', gene, '-------> length:', Seq0.seq_len(sequence))