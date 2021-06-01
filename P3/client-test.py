from Client0 import Client

c = Client('127.0.0.1', 8082)

print('Testing Ping...')
c.talk('"PING"')

print('Testing Get...')
for i in range(0,5):
    msg = 'GET ' + str(i)
    c.talk('"' + msg + '"')

print('Testing Info...')
c.talk('"INFO ACTCGATCGAGCTGAGTCATCTAGCATCACAGT"')

print('Testing Comp...')
c.talk('"COMP ACTCGATCGAGCTGAGTCATCTAGCATCACAGT"')

print('Testing Rev...')
c.talk('"REV ACTCGATCGAGCTGAGTCATCTAGCATCACAGT"')

print('Testing Gene...')
gene_list = ['ADA', 'FRAT1', 'FXN', 'RNU6_269P', 'U5']
for gene in gene_list:
    msg = 'GENE ' + gene
    print('"' + msg + '"')
    c.talk(msg)
