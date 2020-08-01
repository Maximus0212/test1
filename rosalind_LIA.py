import math

def nCr(r,n):
    f = math.factorial
    return f(n)/f(r)/f(n-r)

k = 3
n = 2

result = 0

tot = 2**k

for i in range(n):
    t = ((1/4)**(i)) * ((3/4)**(tot-(i)))
    T = t*nCr(i, tot)
    result += T

print(round(1-result, 3))
