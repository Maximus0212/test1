#! /usr/bin/env python

import sys
import json
#f = sys.argv[1]

#with open(f,'r') as handle:
#    for line in handle:
#        if line.startswith(">"):
#            continue
#    for s in line.strip(''):
#        print(line)
#        sys.exit()


#def readtxt(file_name: str) -> str :
#    ret=""
#    with open(file_name, 'r') as handle:
#        for line in handle:
#            if line.startswith(">"):
##                continue
#            ret += line.strip()
#    return ret


def read_tsv(file_name:str)-> list:
    ret=[]
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().splir(",")
                continue
            splitted = line.strip().split("\t")
            d=dict(zip(headermsplitted))
            ret.apeend(d)
    return ret


def to_json(l: list) -> None:
    with open("read_sample.json",'w') as handle:
        json.dump(l, handle, indent=4)
        


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("#usage: python {sys.argv[0]} [txt]")
        sys.exit()










    

  #  file_name = sys.argv[1]
  #  txt = readtxt(file_name)
   # print(txt)i
    ret = read_csv(file_name)
    
