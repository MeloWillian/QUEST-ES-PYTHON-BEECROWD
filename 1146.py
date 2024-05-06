

n = int(input())
while n != 0:
    l = []
    for i in range(1,n+1):     
        l.append(str(i))
    a = " ".join(l)
    print(a)
    n = int(input())