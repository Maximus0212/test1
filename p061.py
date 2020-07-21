#! /usr/bin/env python


class FASTQ:
    def __init__(self, file_name:str):
        self.file_name = file_name
        self.num = 0
    
    def count_read_Num(self):
        with open(self.file_name, 'r') as handle:
            for line in handle:
                if 
        
