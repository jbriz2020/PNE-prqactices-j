from P0.Seq0 import Seq

def print_seqs(list):
    for i in range(0, len(list)):
        print('Sequence', i, ': (Length: ', list[i].len(), ')', list[i])


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)