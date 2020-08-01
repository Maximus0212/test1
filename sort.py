d = {}


with open("data.txt",'r') as fr:
    for line in fr:
        l = line.strip().split(",")
        gene, val = l[0], l[1]
        d[gene] = val


print(sorted(d.items(), key=lambda x: x[1], reverse=False))


