t = []

for i in range(100):
    a = input()
    t.append(int(a))
    

print(max(t))
print(t.index(max(t))+1)