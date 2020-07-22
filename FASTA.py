import sys

#class FASTA:
#    def __init__(self, file_name):
#        self.file_name = file_name
#        self.count={}

#    def count_base(self):
#        with open(self.file_name, 'r') as handle:
#            for line in handle:
#                if line.startswith(">"):
#                    continue
#                line = line.strip()
#                for s in line:
#                    if s in self.count:
#                        self.count[s] += 1
#                    else:
#                        self.count[s] = 1
class FASTQ:
    def __init__(self, file_name):
        self.file_name = file_name
        self.read_num = 0
        self.base={}
    
    def count_read_num(self):
        cnt = 0
        with open(self.file_name,'r') as handle:
            for line in handle:
                if cnt % 4 == 0:
                    header = line.strip()
                    self.read_num += 1
                elif cnt % 4 == 1:
                    seq = line.strip()
                    for s in seq:
                        if s in self.base:
                            self.base[s] += 1
                        else:
                            self.base[s] = 1
                elif cnt % 4 ==3:
                    qual = line.strip()
                cnt += 1



file_name = sys.argv[1]
#t = FASTA(file_name)
#t.count_base()
#print(t.count)

t=FASTQ(file_name)
t.count_read_num()
print(t.read_num)
print(t.base)
