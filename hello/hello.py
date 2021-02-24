print('hola q talll')
seq = 'CATGTAGACTAG'

def ex(seq):
    largo = len(seq)
    letters = []
    sum = []
    for e in set(seq):
        letters.append(e)
        sum.append(seq.count(e))
    return letters, sum, largo

def acc(z):
    for e in zip(z[0], z[1]):
        print (e[0], ':', e[1])
    print('Total length:', z[2])

acc(ex(seq))
