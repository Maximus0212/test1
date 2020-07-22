#l_fivo = [0,1]

#fivoIn = input("값을넣어봐")
#fivoIn = int(fivoIn)

#for i in range(fivoIn-2):
#    l_fivo.append(l_fivo[-1]+l_fivo[-2])

#print(l_fivo)



#강사님 방법
import sys

def fib(n:int) -> int:
    if n==0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(sys.argv[1])

print(fib(n))






