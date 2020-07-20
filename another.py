#!/usr/bin/env python
#
print("Hello bioinformatic!")

#Variable
import math
r = 3
PI = math.pi
area = PI*r**2
print(area)

#Operator
num1 = 3
num2 = 5
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 ** num2)

#if else
num1 = 3

if num1/2 == 0:
    print(num1, "is even")
else:
    print(num1, "is odd")

#if elif else
num1 = 21
if num1 % 3 ==0 and num1 % 7 ==0:
    print("3의배수,7의배수")

elif num1%3 == 0:
    print(num1,"은 3의 배수")
elif num1%7 ==0:
    print(num1,"은 7의 배수")
else:
    print("둘다아니야")

#6 for
total = 0 #이걸 생각하는게 중요해우쓰

for i in range(1,11):
    total+=i

print(total)

#7 중첩 for 문 

#for i in range(2,9,2):
#    for j in range(1,10,1):
#        print(i, "*", j, "=",i*j)


for i in range(2,10,1):
    for j in range(1,10,1):
        if i % 2 == 0:
            print(f"{i}x{j}={i*j}")

#8 while
num = 5
result = 1

while num>0:#condition
    result*= num 
    num -= 1#탈출

print(result)

#9 function
def greet():
    print('Hello, Bioinformatic')

greet()

#10 
def mySum(num1:int, num2:int) -> None:
    print(f"{num1}+{num2}={num1+num2}")

mySum(2,3)
mySum(4,5)
mySum(9,3)
mySum(3,3)

def mySum(num1:int, num2:int) -> int:
    return num1 + num2
    #print(f"{num1}+{num2}={num1+num2}")

res1 = mySum(2,3)
res2 = mySum(4,5)
res3 = mySum(9,3)
  
print(res1)
print(res2)
print(res3)

#13

#name = input("이름입력:")
#print(f"Hello{name}")

#print(type(name))

#14

word = input("한글자를 입력해:")

if word.isalpha():
    print(f"{word} is alpha")
elif word.isdigit():
    print(f"{word} is digit")
else:
    print("get out")




