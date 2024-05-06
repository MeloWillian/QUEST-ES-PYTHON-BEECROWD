n = int(input())

for i in range (n):
    l = []
    p = int(input())
    for i in range(p):   
        l.append(input())
    if(any(e != l[0] for e in l)):print("ingles")
    else:print(l[0])

