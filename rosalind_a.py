d ={}
with open("rosalind2.txt",'r') as handle:
    for line in handle:
        if line.startswith(">"):
            header = line.strip().split()
            print(header)
            continue
        splitted = line.strip().split()
        
        for s in line.strip():
            if s in d:
                d[s] += 1
            else:
                d[s] =1

        print(d)
