def FindMotif(s1, s2):
    if len(s2) > len(s1):
        s1, s2 = s2, s1
    n = len(s2)
    for i in range(n):
        for j in range(i+1):
            token = s2[j : n-i+j]
            if token in s1:
                return token                

def reform(lines):
    for line in lines:
        if line.startswith(">"):
            a = line.replace(">",'')
            a = a.replace("\n", "")
            id_.append(a)
        else:
            if len(id_) > len(seq):
                line = line.replace("\n",'')
                seq.append(line)
            else:
                line = line.replace("\n",'')
                seq[len(id_)-1] = seq[len(id_) - 1 ] + line
    return id_ ,seq

f = open("rosalind_lcsm.txt", 'r')
lines = f.readlines()
id_ = []
seq = []
id_,seq = reform(lines)
com = ''

for i in range(len(seq)-1):
    if com == '':
        com = FindMotif(seq[i], seq[i+1])
        print(com)
    else:
        if len(com) >= len(FindMotif(seq[i+1],com)):
            com = FindMotif(seq[i+1],com)

print(com)

