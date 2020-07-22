cnt = 0
num = 0

with open("070.vcf",'r') as handle:
    for line in handle:
#        if line.startswith("##"):
#            continue
        if line.startswith("#"):
#            header = line.strip().split("\t")
           # filt_idx = header.index("FILTER")   
            # 파일이 엄청 길고 복잡할때 FILTER가 들어간 곳이 어딘지 알려고
#            filt_idx2 = header.index("ID")
            continue
#        splitted = line.strip().split('\t')
       # if splitted[filt_idx]=="PASS": #라고 다시 바꿔쓰면 안정적이 되버렷
        #    cnt += 1
        splitted = line.strip().split('\t')
        chrom = splitted[0]
        pos = splitted[1]
        id_ = splitted[2]
        ref = splitted[3]
        alts = splitted[4].split(',')
  
        for alt in alts:
            cnt += 1

print(cnt)



      
#        if splitted[filt_idx2] != ".":
#            print(f"{chrom}-{pos}-{ref}-{alt}-{id_}")
#print(cnt)










#용재방법
#num =0

#with open("070.vcf",'r')as handle:
#    for line in handle:
#        if line.startswith("#"):
#            continue
#        else:
#            Filter = line.strip().split('\t')
#            if "PASS" in Filter:
#                num += 1

#print(num)
            


#        splitted = line.strip().split('\t')
#        if splitted[6] == "PASS"
#            cnt += 1



