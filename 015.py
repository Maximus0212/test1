#! /usr/bin/env python

import sys

d={}

f = sys.argv[1]

with open(f,'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for s in line.strip():
            if s in d:
                d[s]+=1
            else:
                d[s]=1

print(d)
