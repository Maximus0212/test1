s_l = ['ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG','ATCGGTCGAA','ATCGGTCGAGCGTGT']
ref_seq = []
#seq = []

result_seq = []

for i in range(len(s_l)):
    if s_l[i]== s_l[0]:
        ref_seq.append(s_l[i])
    elif s_l[i] in s_l[0]:
        ind =s_l[0].index(s_l[i])     # 33 67
        len_seq = len(s_l[i])         # 10 15
        #print(int(ind)+int(len_seq))  # 43 82
        print(len(s_l[0]))
        


#result = s_l[0][0:s_l[0].index(s_l[1])], s_l[0][s_l[0].index(s_l[1])+len(s_l[1]):s_l[0].index(s_l[2])], s_l[0][s_l[0].index(s_l[2])+len(s_l[2]):len(s_l[0])]


      
#result_seq += result
#
#print(result_seq) 
#A = ''.join(result_seq)
#print(A)

#print(A.replace('T','U'))









idx = s_l[0].index[i+1]
len_i = s_l[i+1]

for i in range(3):  # i = 0 1 2 

    result = s_l[0][0:idx(1)], s_l[0][idx(1)+len_(1):idx(2)], s_l[0][idx(2)+len_(2):idx(3)] , s_l[0][idx[3]+len_(3):idx(4)], ]
                


처음 들어가는 수가 0 일거란 말야

0+1 0+1 0+1 0+2 0+2 0+2 0+3 0+3 0+3 0+4 0+4 0+4 0+5 0+5 0+5 ............ 0+i 0+i 0+i

idx(i+1)
len_(i+1)

따로빼고
0:idx(1)

for i in range():
    idsx(i)+len(i) : idx(i+1)

나온 결과값들을 리스트로 저장 

너도 따로뺴
idx(i)+len(i) : len(s_l[0])


first_list = s_l[0][0:idx(1)]

middle_list = []
for i in range(len(s_l)):
    middle_seq = s_l[0][idx(x)+len(i) : idx(i+1)]

last_list = s_l[0][idx(len(s_l)+len(len(s_l)) : len(s_l[0])]


































