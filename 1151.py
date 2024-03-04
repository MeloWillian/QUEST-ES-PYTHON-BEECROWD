l = [0,1]
b = int(input())
idx1 = 0
idx2 = 1

for i in range(b-1):
    b = l[idx1]+l[idx2]
    l.append(b)
    idx1 +=1
    idx2 +=1

print(" ".join(map(str,l)))

