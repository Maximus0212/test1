l = []
l_h = []
d = {}

with open("multi.fasta",'r') as handle:
    for line in handle:
        if line.startswith(">"):
            header = line.strip().split('\n')
            l_h.append(header)
        else:
            l += line.strip().split('\n')

for k,v in enumerate(l):
    Seq = "Seq" +str(k+1)
    d[Seq] = {"A":0, "T":0, "C":0, "G":0}
    for s in v:
        if s == "A":
            d[Seq]["A"] += 1
        elif s == "T":
            d[Seq]["T"] += 1 
        elif s == "C":
            d[Seq]["C"] += 1
        elif s == "G":
            d[Seq]["G"] += 1
        
    GCsum =d[Seq]['G'] + d[Seq]['C']
    Sum = d[Seq]['A'] + d[Seq]['T'] + d[Seq]['G'] + d[Seq]['C']
    print((GCsum/Sum)*100)

print(d)


""" 
i = 0
while i < len(l):
    Seq = "Seq" + str(i+1)
    d[Seq] = {"A":0, "T":0, "C":0, "G":0}
    
    for s in l[i]:
        if s == "A":
            d[Seq]["A"] += 1
        elif s == "T":
            d[Seq]["T"] += 1
        elif s == "C":
            d[Seq]["C"] += 1
        elif s == "G":
            d[Seq]["G"] += 1
        
    i += 1      
"""


'''

i = 0

while i < len(l):
    Seq = "Seq" + str(i+1)
    d[Seq] = {"A":0, "T":0, "C":0, "G":0}
    
    j = 0
    while j < len(l[i]):
        if l[i][j] == "A":
            d[Seq]["A"] += 1
        elif l[i][j] == "T":
            d[Seq]["T"] += 1
        elif l[i][j] == "C":
            d[Seq]["C"] += 1
        elif l[i][j] == "G":
            d[Seq]["G"] += 1
                
        j += 1
    i += 1
print(d) 
''' 
