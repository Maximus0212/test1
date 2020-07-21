#! /usr/bin/env python

#f = 'read_sample.csv'

#with open(f,'r') as fr:
#    for line in fr:
#        print(line.strip().split(","))

import sys

def read_csv(file_name):
    ret=[]
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split(",")
                continue
            splitted = line.strip().split(",")
            d= dict(zip(header, splitted))
            ret.append(d)
    return ret


