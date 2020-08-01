import json
import sys

#class FASTA:
#    def __init__(self, file_name):
#        self.file_name=file_name
#        self.base = {}

#    def count_base(self):
#        with open(self.file_name, 'r') as handle:
#             for line in handle:
#                if line.startswith(">"):
#                    continue
#                for s in line.strip('\n'):
#                    if s in self.base:
#                     self.base[s] += 1
#                    else:
#                        self.base[s] = 1
#        return self.base
 

#def write_json(d, file_name):
#   with open(file_name,'w') as handle:
#       json.dump(d, handle, indent=4)

with open("059.fasta", 'r')as handle:
    l = []
    for line in handle:
        if line.startswith(">"):
            continue
        sequence = line.strip().split('\n')
        l += sequence


dic = {'A':'t', 'T':'a', 'C':'g', 'G':'c'}
str_ = ""


for s in l:
    for a in s:
        str_ += dic[a]

recomp = str_.upper()
print(recomp)


#recomp_l = []

#for s in l:
#    s = s.replace("A","t")
#    s = s.replace("T","a")
#    s = s.replace("C","g")
#    s = s.replace("G","c")
#    
#    s = s.upper()
#    
#    recomp_l.append(s)


#print(l)

#print(recomp_l)

#file_name = sys.argv[1]

#write_json(d, "subject.json")
#t = FASTA(file_name)
#T = t.count_base() 
#print(t.count_base())
#write_json(T, "subject.json")
