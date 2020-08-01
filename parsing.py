import sys
import json

#def read_txt(file_name):
#    ret= " " 
#    with open(file_name, 'r') as handle:
#        for line in handle:
#            if line.startswith(">"):
#                continue
#            ret += line.strip()
#    return ret

def read_csv(file_name):
    ret = []
    with open(file_name, 'r')as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split(',')
                continue
            splitted= line.strip().split(',')
            d = dict(zip(header,splitted))
            ret.append(d)
    return ret

def read_tsv(file_name):
    ret = []
    with open(file_name, 'r')as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split('\t')
                continue
            splitted= line.strip().split('\t')
            d = dict(zip(header,splitted))
            ret.append(d)
    return ret

def write_json(l, file_name):
    with open(file_name, 'w') as handle:
        json.dump(l, handle, indent=4)

def read_json(file_name):
    with open(file_name, 'r') as handle:
        l = json.load(handle)
    return l


file_name = sys.argv[1]
#t = read_txt(file_name)
#print(t)
#t = read_csv(file_name)
#ret = read_tsv(file_name)
#print(ret)
#write_json(t, "overtherainbow.json")
t=read_json(file_name)
print(t)




