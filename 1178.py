l = [0]*100
a = float(f"{float(input()):.4f}")
for i in range(len(l)):
    l[i] = a
    a = a/2

s = 0
for p in l:
    print(f"N[{s}] = {p:.4f}")
    s+=1