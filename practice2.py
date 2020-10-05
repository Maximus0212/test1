s_l = ['QQQTAGWWWCGGFFFFFATACMMMM','TAG','CGG','ATAC']

ref_seq = []

first_list = []
middle_list = []
last_list = []

result_list = []

#middle_seq = s_l[0][s_l[0].index(s_l[1])+len(s_l[1]) : s_l[0].index(s_l[2])]

#print(middle_seq)

#print(s_l[3] in s_l[0])


for i in range(len(s_l)):
    if i == 0:
        first_seq = s_l[0][0:s_l[0].index(s_l[1])]
        print(first_seq)
##    elif i==1:
##        first_seq = s_l[0][0:s_l[0].index(s_l[1])]
##        print(first_seq)
        first_list.append(first_seq)
        
    elif i == len(s_l)-1:   # 3
        last_seq = s_l[0][s_l[0].index(s_l[i])+len(s_l[i]) : len(s_l[0])]
        print(last_seq)
        last_list.append(last_seq)
#        continue
#    elif i == i:

    elif s_l[i] in s_l[0]:
#        if i == 1:
#            fisrt_seq = s_l[0][0:s_l[0].index(s_l[i])]
#            print(first_seq)
#        else:
        middle_seq = s_l[0][s_l[0].index(s_l[i])+len(s_l[i]) : s_l[0].index(s_l[i+1])]
        print(middle_seq) 
        middle_list.append(middle_seq)

#    elif i == len(s_l):
#        last_seq = s_l[0][s_l[0].index(s_l[i])+len(s_l[i]) : len(s_l[0])]
#        print(last_seq)
        #last_list.append(last_seq)
#        continue
#    elif i == i:
        

#idx(i) = s_l[0].index(s_l[i])

#len_(i) = len(s_l[i])
      
#first 만들기
#first_seq = s_l[0][0:idx(1)]
#first_seq = s_l[0][0:s_l[0].index(s_l[1])]
#first_list.append(first_seq)

# middle 만들기
#for i in range(len(s_l)):
#    middle_seq = s_l[0][idx(i)+len_(i) : idx(i+1)]
#    middle_list.append(middle_seq)
      

#last 만들기
#last_seq = s_l[0][idx(len_(s_l))+len_(len(s_l)) : len_(s_l[0])]
#last_seq = s_l[0][s_l[0].index(
#last_list.append(last_seq)


print(first_list)
print(middle_list)
print(last_list)

#result_list.append(first_list)
#result_list.append(middle_list)
#result_list.append(last_list)

result_list = first_list + middle_list + last_list

print(''.join(result_list))





















