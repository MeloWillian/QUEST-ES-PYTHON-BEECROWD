t = []

for i in range(101):
    a = int(input())
    t.append(a)
    

print(max(t))
print(t.index(max(t))+1)