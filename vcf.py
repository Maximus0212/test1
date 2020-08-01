import pandas as pd
from matplotlib import pyplot as plt

#cnt = 0

d = {"snp:":0 , "del:":0, "ins:":0}

with open("070.vcf",'r') as handle:
    for line in handle:
#        if line.startswith("##"):
#            continue
        if line.startswith("#"):
#            header = line.strip().split('\t')
#            filt_idx = header.index("FILTER")
#            id_idx = header.index("ID")
#            chrom_idx = header.index("CHROM")
#            pos_idx = header.index("POS")
#            ref_idx = header.index("REF")
#            alt_idx = header.index("ALT")
            continue            
        splitted = line.strip().split('\t')
       # if splitted[filt_idx] == "PASS" :
           # cnt += 1
        chrom = splitted[0]
        pos = splitted[1]
        id_ = splitted[2]
        ref = splitted[3]
#        alt = splitted[4]
        alts = splitted[4].split(',')
#        if splitted[id_idx] != "." :
#            print(f"{chrom}-{pos}-{ref}-{alt}-{id_}")
        for alt in alts:
            if len(ref) == len(alt): #SNP
                d["snp:"] += 1
            elif len(ref) > len(alt): #deletion
                d["del:"] += 1
            elif len(ref) < len(alt): #Insertion
                d["ins:"] += 1
            else:
                raise    
            cnt += 1

        
print(cnt)
print(d)
df = pd.DataFrame([d])
print(df)
df.plot.bar()
plt.savefig("v.png")





