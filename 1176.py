for i in range(int(input())):
    l = [0,1]
    a= int(input())
    for i in range(a):
       l.append(l[-1]+l[-2])
    print(f"Fib({a}) = {l[-2]}")
