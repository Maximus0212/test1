import sys

fasta_dict = {}
seq = ''

if len(sys.argv) != 2:
    print(f'#usage: python {sys.argv[0]} [fasta.file]')
    sys.exit()


f = sys.argv[1]
header = None
with open(f, 'r') as handle:
    for line in handle:
        line = line.strip()
        if line.startswith(">"):
            if header:
                fasta_dict[header] = seq
            header = line[1:]
            fasta_dict[header] = ''
            seq = ''
        else:
            seq += line
    if header:
        fasta_dict[header] = seq

#print(fasta_dict)
k_l = []
v_l = []
for k,v in fasta_dict.items():
    k_l.append(k)
    v_l.append(v)
#print(k_l)
#print(v_l)

for i in range(len(k_l)):
    for j in range(0,len(k_l)):
        if v_l[i][-3:] == v_l[j][:3] and i != j :
            print(k_l[i], k_l[j])


