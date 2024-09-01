l = []

for i in range(20):
    l.append(int(input()))

l.reverse()

c = 0
for p in l:
    print(f"N[{c}] = {p}")
    c+=1