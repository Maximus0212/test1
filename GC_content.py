import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [fasta.file]")
    sys.exit()

fasta_dict = {}
header = None
seq =""

with open(sys.argv[1], 'r') as handle:
    for line in handle:
        line = line.rstrip()
        if line.startswith(">"):
            if header:
                fasta_dict[header] = seq
            header = line[1:]
            fasta_dict[header] = ""
            seq = ""
        else:
            seq += line
    if header:
        fasta_dict[header] = seq

#print(fasta_dict)

GC_content_dict = {}

for k,v in fasta_dict.items():
    A = v.count("A")
    T = v.count("T")
    C = v.count("C")
    G = v.count("G")
    GC_content = (G+C)/(G+T+A+C) * 100
    GC_content_dict[k] = GC_content

#print(GC_content_dict)

all_values = GC_content_dict.values()
max_GC = max(all_values)



for k,v in GC_content_dict.items():
    if v == max_GC:
        print(k)
        print(v)


