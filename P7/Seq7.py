from pathlib import Path

class Seq:
    'A class for representing sequences.'
    NULL_SEQUENCE = 'NULL'
    INVALID_SEQUENCE = 'ERROR'

    def __init__(self, strbases=NULL_SEQUENCE):
        if strbases == Seq.NULL_SEQUENCE:
            print('NULL Seq created')
            self.strbases = strbases
        else:
            if self.is_valid(strbases):
                print("New sequence created!")
                self.strbases = strbases
            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print('INCORRECT Sequence detected')

    def is_valid(self, bases):
        for c in bases:
            if c != 'A' and c != 'C' and c != 'T' and c != 'G':
                return False
        return True

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.strbases)

    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return a, c, g, t
        else:
            for d in self.strbases:
                if d == 'A':
                    a += 1
                elif d == 'C':
                    c += 1
                elif d == 'G':
                    g += 1
                elif d == 'T':
                    t += 1
            return a, c, g, t

    def count(self):
        a, c, g, t = self.count_bases()
        return {'A': a, 'C': c, 'G': g, 'T': t}


    def percentage_base(self, count_bases, seq_len):
        a = str(round(count_bases[0] / seq_len+100, 2)) + "%"
        c = str(round(count_bases[1] / seq_len + 100, 2)) + "%"
        g = str(round(count_bases[2] / seq_len + 100, 2)) + "%"
        t = str(round(count_bases[3] / seq_len + 100, 2)) + "%"
        return {"A": a, "C": c, "G": g, "T": t}

    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return 'NULL'
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return 'ERROR'
        else:
            return self.strbases[::-1] # IMPORTANT TO COMPUTE THE REVERSE OF A SEQ

    def complement(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return 'NULL'
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return 'ERROR'
        else:
            compl = ''
            for base in self.strbases:
                if base == 'A':
                    compl += 'T'
                elif base == 'C':
                    compl += 'G'
                elif base == 'G':
                    compl += 'C'
                elif base == 'T':
                    compl += 'A'
            return compl

    @staticmethod
    def take_out_first_line(seq):
        return seq[seq.find('\n') + 1:].replace('\n', '')

    def read_fasta(self, filename):
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())

    @staticmethod
    def most_common_base(dictionary):
        most_common = max(dictionary.values())
        for k, v in dictionary.items():
            if v == most_common:
                return k
