f = "rosalind2.txt"

A, C, G, T = 0, 0, 0, 0

with open(f,'r')as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        else:
            seq = line.strip()
            A += seq.count("A")
            T += seq.count("T")
            C += seq.count("C")
            G += seq.count("G")

print(A, T, C, G)
