l = 0
p = 0
for i in range(6):
    a=float(input())
    if(a > 0): p+=1; l+=a
    
print(p,"valores positivos")
print(f"{(l/p):.1f}")