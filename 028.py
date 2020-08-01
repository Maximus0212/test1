import sys

def comp1(seq):
    comp = ""
    for s in seq:
        if s == 'A':
            comp += 'T'
        elif s == 'C':
            comp += 'G'
        elif s == 'G':
            comp += 'C'
        elif s == 'T':
            comp += 'A'
    return comp

def comp2(seq):
    d_comp = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    comp=''
    for s in seq:
        comp += d_comp[s]
    return comp



seq = sys.argv[1]
#c1 = comp1(seq)
c2 = comp2(seq)
#print(c1)
print(c2)
