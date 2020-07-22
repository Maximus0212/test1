import pandas as pd
from matplotlib import pyplot as plt


d = {"snp":0, "del":0, "ins":0}

with open("070.vcf",'r')as handle:
    for line in handle:
        if line.startswith("#"):
            continue

        splitted = line.strip().split('\t')
        chrom = splitted[0]
        pos = splitted[1]
        ref = splitted[3]
        alts = splitted[4].split('\t')

        for alt in alts:
            if len(ref) == len(alt):#snp
                d["snp"] += 1
            elif len(ref) > len(alt):#deletion
                d["del"] += 1
            elif len(ref) < len(alt):#insertion
                d["ins"] += 1
            else: #방어적코딩
                raise #혹시나 생각치 못한 것이 있으면 오류를 만들면서 멈추게 해야되용

print(d)
df = pd.DataFrame([d])
print(df)
df.plot.bar()
plt.savefig("v.png")
