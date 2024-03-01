A = input()

l = A.split(" ")

b = int(l.pop(1))
a = float(l.pop(0))

print(f"{(a / b):.2f}")