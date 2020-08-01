#! /usr/bin/env python
import os
import sys

chrs=''
for i in range(0,25):
    if i== 23 : i='X'
    elif i==24 : i='Y'
    elif i==0 : i='M'
    os.system("wget http://hgdownload.soe.ucsc.edu/goldenPath/hg19/chromosomes/chr"+str(i)+".fa.gz")
    chrs+="chr"+str(i)+".fa "


chrs=chrs.strip()
os.system("cat "+chrs+" > hg19.fa")
