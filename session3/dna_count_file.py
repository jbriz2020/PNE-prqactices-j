with open ('dna.txt', 'r') as f:
    a = 0
    c = 0
    t = 0
    g = 0
    for line in f:
        for e in line:
            if e == 'A':
                a += 1
            elif e == 'C':
                c += 1
            elif e == 'G':
                g += 1
            elif e == 'T':
                t += 1
    print(a, c, t, g)