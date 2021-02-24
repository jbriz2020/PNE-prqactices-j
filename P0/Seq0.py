from pathlib import Path

def seq_ping():
    print('OK.')

def body(sequence):
    return sequence[sequence.find('\n') + 1:].replace('\n','')

def seq_read_fasta(filename):
    sequence = body(Path(filename).read_text())
    return sequence

def seq_len(seq): #calc total number of bases
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base) #es mejor ir iterando eeeh

def seq_count(seq):
    a, c, g, t = 0, 0, 0, 0
    for d in seq:
        if d == 'A':
            a += 1
        elif d == 'C':
            c += 1
        elif d == 'G':
            g += 1
        elif d == 'T':
            t += 1
    return {'A': a, 'C': c, 'G': g, 'T': t}