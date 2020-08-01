cnt = 0
read_num = 0
d = {}
with open("061.fastq",'r') as handle:
    for line in handle:
        if cnt % 4 == 0:
            read_num += 1
        

        elif cnt %4 == 1:
            for s in line.strip():
                if s in d:
                    d[s] += 1
                else:
                    d[s] =1

        cnt += 1
print(d)      
#print(cnt)
#print(read_num)
