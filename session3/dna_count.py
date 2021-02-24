seq = 'CATGTAGACTAG'

def ex(seq):
    largo = len(seq)
    a = 0
    c = 0
    t = 0
    g = 0
    for e in seq:
       if e == 'A':
           a += 1
       elif e == 'C':
           c += 1
       elif e == 'G':
           g +=1
       elif e == 'T':
           t += 1
    return a, c, g, t, largo

def impr(count):
    print('Total length:', count[4])
    print('A:', count[0], '\nC:', count[1], '\nG:', count[2], '\nT:', count[3])

impr(ex(seq))
