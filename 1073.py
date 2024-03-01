A = int(input())

def valor (a):
    if(a % 2 == 0): return a+2
    else:return a

for i in range(2,valor(A),2):print(f"{i}^2 = {i**2}")
