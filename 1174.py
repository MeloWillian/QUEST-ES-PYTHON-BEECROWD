l = [0] * 100
for i in range(100):
    a = float(input())
    l[i] = a
c = 0
for p in l:
    if p <= 10:
        print(f"A[{c}] = {p}")
    c+=1