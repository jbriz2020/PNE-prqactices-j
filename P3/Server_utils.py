# funciones

from Seq1 import Seq

def print_colored(msg, color):
    import termcolor
    import colorama
    colorama.init(strip='False')
    print(termcolor.colored(msg,color))

def format_command(command):
    return command.replace('\n','').replace('\r','')

def ping(cs):
    print_colored('PING command', 'green')
    response = 'OK!'
    print(response)
    cs.send(response.encode())

def get(list_sequences, cs, argument):
    print_colored('GET' + str(argument.replace('"','')), 'yellow')
    response = list_sequences[int(argument.replace('"','').replace('"',''))]
    print(response)
    cs.send(response.encode())

def info(arg, cs): # total length, number of bases and their percentages
    seq = Seq(arg.replace('"',''))
    sl = Seq.len(seq)
    a, c, g, t = Seq.count_bases(seq)
    p_a = (100 * a / sl)   # p = percentage
    p_c = (100 * c / sl)
    p_g = (100 * g / sl)
    p_t = (100 * t / sl)

    response = 'Sequence: ' + str(seq) + '\nTotal length: ' + str(sl) + '\nA: ' + str(a) + '(' + str(p_a) + '%)\nC: ' + str(c) + '(' + str(p_c) + '%)\nG: ' + str(g) + '(' + str(p_g) + '%)\nT: ' + str(t) + '(' + str(p_t) + '%)'
    print(response)
    cs.send(response.encode())


def comp(arg, cs):
    print_colored('Complement','yellow')
    seq = Seq(arg.replace('"',''))
    c_seq = Seq.complement(seq)
    print('Complement sequence:', c_seq)
    cs.send(str(c_seq).encode()) #you can only encode strings #lo convertimos en str pq era una Seq!

def rev(arg, cs):
    print_colored('Reverse','yellow')
    seq = Seq(arg.replace('"',''))
    r_seq = Seq.reverse(seq)
    print('Reverse sequence:', r_seq)
    cs.send(str(r_seq).encode())

def gene(arg, cs):
    print_colored('Gene','yellow')
    filename = './sequences downloaded/' + arg.replace('"','')
    seq_null = Seq() # hay q crear una null seq para poder leer un method q no es static
    seq_null.read_fasta(filename)
    print(seq_null)
    cs.send(str(seq_null).encode())


# seguir ejs s11 p3 (wiki)
# cs.send sirve para mandarlo al cliente
# print para imprimirlo dentro del servidor