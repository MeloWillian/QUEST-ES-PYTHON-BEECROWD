import math

A = input()
l = A.split(" ")

c = int(l.pop(2))
b = int(l.pop(1))
a = int(l.pop(0))

s = (c+b+a) / 2

val = math.sqrt((s*(s-a)*(s-b)*(s-c)))

print(f"{val:.3f} m2")