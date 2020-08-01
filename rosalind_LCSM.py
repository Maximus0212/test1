import sys

f = sys.argv[1]
header = []
seq = []

with open(f, 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            head = line.lstrip('>').strip()
            header.append(head)
        else:
            seq.append(line.strip())


fasta_dict = dict(zip(header, seq))

print(fasta_dict)

#for header in fasta_dict:
#    Seq = fasta_dict[header].split('\n')
