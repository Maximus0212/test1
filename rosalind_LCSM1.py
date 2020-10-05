import sys
  
f = sys.argv[1]
header = []
seq = [] 
with open(f, 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            head = line.lstrip('>').strip()
            header.append(head)
        else:
            seq.append(line.strip())

#print(seq)


#seq =['acaac', 'agct','acgggct']

sor_list = sorted(seq,key=len) #길이순으로 정렬('agct','asdasd','asdsadasd')
#print(sor_list)

#if sor_list[0][0:1] in sor_list[1] and sor_list[0][0:1] in sor_list[2]:
#    word= sor_list[0][0:1]

result = []

for s in range(len(header)):
#    print(s)  # 0 1 2 
    
   for i in range(len(sor_list[0])):

        for j in range(i+1, i+len(sor_list[0])):

            if sor_list[0][i:j] in sor_list[s]:

                word = sor_list[0][i:j] 

                result.append(word)

#print(max(result, key=len))
#        else: 
#            print('F')













