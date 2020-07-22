l1 = ['A','T','C','G']
l2 = ['A','T','C','G']
ltmp = []
def mer(l1,l2,n):
    if n == 1:
        return l2
    for i in l1:
        for j in l2:
            ltmp.append(i+j)
    return mer(l2, ltmp, n-1)

print(mer(l1,l2,3))
