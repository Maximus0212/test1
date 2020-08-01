import os
import sys

chrs =""
for i in range(0,25):
    if i == 0: i='M'
    elif i == 23: i='X'
    elif i == 24: i='Y'
    os.system(f"wget http://hgdownload.soe.ucsc.edu/goldenPath/hg38/chromosomes/chr{i}.fa.gz")

    chrs += "chr"+str(i)+".fa"

chrs = chrs.strip()
cat_file = "hg19.fa"
dict_file = "hg19.dict"

os.system("cat"+chrs+">"+cat_file)

os.system("bwa index -a bwtsw",cat_file)

os.system("samtools faidx",cat_file)

os.system("java -jar /BiO/Install/picard-tools-2.22.3/picard.jar CreateSequenceDictionary","R="+cat_file,"O="+dict_file)






