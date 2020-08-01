import sys

class BED:
    def __init__(self, file_name):
        self.file_name = file_name
        self.total = 0
        self.len = 0

    def Total(self):
        with open(self.file_name, 'r') as handle:
            for line in handle:
                splitted = line.strip().split()
                start = int(splitted[1])
                end = int(splitted[2])
                self.total += end -start

    def length(self):
        l = []
        z = []
        with open(self.file_name, 'r') as handle:
            for line in handle:
                splitted = line.strip().split()
                chrom = splitted[0]
                z.append(chrom)
                start = int(splitted[1])
                end = int(splitted[2])
                self.len = end - start
                l.append(self.len)
                d =dict(zip(z,l)) #한번만 나와줘 제발
            print(d)
#    
file_name = sys.argv[1]
t = BED(file_name)
t.Total()
t.length()
print(t.total)
print(t.len)
