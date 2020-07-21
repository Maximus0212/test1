#! /usr/bin/env python

#Seq1 = "ATGTTATAG"

#for i in range(0,len(Seq1),3):
#    print(i) #0,3,6

#    print(i, Seq1[i]) #인덱싱

#    print(Seq1[i:i+3]) # splicing
#    print(i, i+3, Seq1[i]) 

#print(Seq1[0:3])
#print(Seq1[3:6])
#print(Seq1[6:9])

#print(Seq1[::-1])
import sys
def comp1(seq: str)->str:
    comp = ""
    for s in seq:
        if s == 'A':
            comp += "T"
        elif s == 'T':
            comp += "A"
        elif s == 'C':
            comp += "G"
        elif s == 'G':
            comp += "C"
    return comp

def comp2(seq: str)->str:
    d_comp = {"A":"T","T":"A","C":"G","G":"C"}
    comp = ""
    for s in seq:
        comp += d_comp[s]
    return comp

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("#usage: python {sys.argv[0]} [string]")
        sys.exit()

    seq = sys.argv[1]
    c1 = comp1(seq)
    c2 = comp2(seq)
    print(seq)
    print(c1)
    print(c2)
