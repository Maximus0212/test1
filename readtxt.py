import sys
import json

def read_txt(file_name: str) -> str:
    ret='' # 빈 string
    with open(file_name,'r') as handle:
        for line in handle:#한줄 씩 받기
            if line.startswith(">"):
                continue
            else:
                ret += line.strip()
    return ret 

def read_csv(file_name:str)-> list:
    ret = []
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split(",") #나중에 출력
                continue
            else:
                splitted = line.strip().split(",")
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret

def read_tsv(file_name : str) -> list:
    ret = []
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split("\t")
                continue
            splitted = line.strip().split("\t")
            d=dict(zip(header, splitted))
            ret.append(d)
    return ret

def write_json(l:list, file_name:str)->None:
    with open(file_name,'w') as handle:
        json.dump(l, handle, indent=4) #들여쓰기한거

def read_json(file_name:str)-> list:
    with open(file_name,'r') as handle:
        l = json.load(handle)
    return l 


    file_name = sys.argv[1]
    ret = read_csv(file_name)
    write_json(ret)




















    file_name = sys.argv[1]
    txt = read_txt(file_name)
    print(txt)
