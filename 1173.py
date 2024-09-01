a = int(input())
l = [a]
for i in range(9):
    l.append(a*2)
    a =a*2
c = 0
for p in l:
    print(f"N[{c}] = {p}")
    c+=1