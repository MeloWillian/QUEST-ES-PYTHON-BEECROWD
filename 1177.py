l = [0] * 1000
a= int(input())
b = 0  
for i in range(len(l)):    
    l[i] = b
    b+=1
    if(b==a):b=0

c=0
for p in l:
    print(f"N[{c}] = {p}")
    c+=1