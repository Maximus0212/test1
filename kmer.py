#재귀하는중 (kmer)

l1 = ['A','T','C','G']
l2 = ['A','T','C','G']
#ltmp = [] 여따 넣으면 시간이 굉장히 오래 걸리면서 안끝날거에염i -> 죽었음

#def mer(l1, l2 ,n):
#    if n == 1 :
#        return l2
#    ltmp = []
#    for i in l1:
#        for j in l2:
#            ltmp.append(i+j)
#    return mer(l2, ltmp, n-1)



#print(mer(l1,l2,3))


#강사님

import sys

def mer(l1,l2,n):
    if n == 1 :
        return l2
    ltmp = []
    for s1 in l1:
        for s2 in l2:
            ltmp.append(s1+s2)

    return mer(l1,ltmp,n-1)


l1 = ['A','T','C','G']
l2 = ['A','T','C','G']
n = int(sys.argv[1])

print(mer(l1,l2,n))
