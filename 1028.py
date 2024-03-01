import math

A = int(input())
l = []

for i in range(0,A):
    var = list(map(int,input().split()))
    l.append(math.gcd(var[0], var[1]))
    
for i in l: print(i)
    