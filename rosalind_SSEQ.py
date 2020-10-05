header = []

with open("rosalind_sample.txt", 'r') in handle:
    for line in handle:
        if line.startswith(">"):
            header = line.strip()
        print(header)
