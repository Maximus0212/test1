#! /usr/bin/env python

import sys

seq1 = sys.argv[1]

for i in range(0,len(seq1),1):
    if seq1[i:i+2] =="TT":
        print(i, i+2, seq1[i:i+2])



