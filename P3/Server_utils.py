# funciones

from Seq1 import Seq
import termcolor

def print_colored(msg, color):
    import termcolor
    import colorama
    colorama.init(strip='False')
    print(termcolor.colored(msg,color))

def format_command(command):
    return command.replace('\n','').replace('\r','')

def ping(cs):
    termcolor.cprint('PING command', 'green')
    response = 'OK!'
    print(response)
    cs.send(response.encode())


def get(list_sequences, cs, argument):
    termcolor.cprint('GET ' + str(argument.replace('"','')), 'yellow')
    response = list_sequences[int(argument.replace('"','').replace('"',''))-1]
    print(response)
    cs.send(response.encode())

def info(arg, cs): # total length, number of bases and their percentages
    termcolor.cprint('INFO', 'yellow')
    seq = Seq(arg.replace('"',''))
    sl = Seq.len(seq)
    a, c, g, t = Seq.count_bases(seq)
    p_a = round((100 * a / sl),1)   # p = percentage
    p_c = round((100 * c / sl),1)
    p_g = round((100 * g / sl),1)
    p_t = round((100 * t / sl),1)
    response = 'Sequence: ' + str(seq) + '\nTotal length: ' + str(sl) + '\nA: ' + str(a) + ' (' + str(p_a) + '%)\nC: ' + str(c) + ' (' + str(p_c) + '%)\nG: ' + str(g) + ' (' + str(p_g) + '%)\nT: ' + str(t) + ' (' + str(p_t) + '%)'
    print(response)
    cs.send(response.encode())


def comp(arg, cs):
    print_colored('COMP','yellow')
    seq = Seq(arg.replace('"',''))
    c_seq = Seq.complement(seq)
    print('Complement sequence:', c_seq)
    cs.send(str(c_seq).encode()) #you can only encode strings #lo convertimos en str pq era una Seq!

def rev(arg, cs):
    termcolor.cprint('REV','yellow')
    seq = Seq(arg.replace('"',''))
    r_seq = Seq.reverse(seq)
    print('Reverse sequence:', r_seq)
    cs.send(str(r_seq).encode())

def gene(arg, cs):
    termcolor.cprint('GENE','yellow')
    filename = './sequences downloaded/' + arg.replace('"','')
    seq_null = Seq() # hay q crear una null seq para poder leer un method q no es static
    seq_null.read_fasta(filename)
    print(seq_null)
    cs.send(str(seq_null).encode())



# cs.send sirve para mandarlo al cliente
# print para imprimirlo dentro del servidor