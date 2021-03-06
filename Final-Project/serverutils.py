# funciones

from Seq1 import Seq
from pathlib import Path
from jinja2 import Template


def read_template_html_file(filename):
    content = Template(Path(filename).read_text())
    return content


def print_colored(msg, color):
    import termcolor
    import colorama
    colorama.init(strip='False')
    print(termcolor.colored(msg,color))



def info(seq): # total length, number of bases and their percentages
    seq = Seq(seq)
    a, c, g, t = seq.count_bases()
    sl = seq.len()
    pa = round((100 * a / sl),1)   # p = percentage
    pc = round((100 * c / sl),1)
    pg = round((100 * g / sl),1)
    pt = round((100 * t / sl),1)
    result = ['Total length: ' + str(sl), 'A: ' + str(a) + ' (' + str(pa) + '%)', 'C: ' + str(c) + ' (' + str(pc) + '%)', 'T: ' + str(t) + ' (' + str(pt) + '%)', 'G: ' + str(g) + ' (' + str(pg) + '%)']
    context = {
        'operation': 'info',
        'sequence': seq,
        'result': result,
        'len_r': len(result)
    }
    contents = read_template_html_file('./html/operation.html').render(context=context)
    return contents


def comp(seq):
    seq = Seq(seq)
    c_seq = Seq.complement(seq)
    context = {
        'operation': 'comp',
        'sequence': seq,
        'result': c_seq
    }
    contents = read_template_html_file('./html/operation.html').render(context=context)
    return contents


def rev(seq):
    seq = Seq(seq)
    r_seq = Seq.reverse(seq)
    context = {
        'operation': 'rev',
        'sequence': seq,
        'result': r_seq
    }
    contents = read_template_html_file('./html/operation.html').render(context=context)
    return contents


def gene(seq_name):
    PATH = './sequences_downloaded/' + seq_name
    s1 = Seq()
    s1.read_fasta(PATH)
    context = {
        'gene_name': seq_name,
        'gene_contents': s1.strbases
    }
    contents = read_template_html_file('./html/gene.html').render(context=context)
    return contents


# cs.send sirve para mandarlo al cliente
# print para imprimirlo dentro del servidor