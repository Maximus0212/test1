import sys

class FASTQ:
    def __init__(self, file_name):
        self.file_name = file_name
        self.read_num = 0
        self.base = {}

    def count_read_num(self):
        cnt = 0
        with open(self.file_name, 'r') as handle:
            for line in handle:
                header = line.strip()
                self.read_num += 1
