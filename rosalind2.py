from Bio import SeqIO

record = SeqIO.read("rosalin2.txt",'fasta')

A = record.seq.count('A')
T = record.seq.count('T')
C = record.seq.count('C')
G = record.seq.count('G')

print(A, T, C, G)
