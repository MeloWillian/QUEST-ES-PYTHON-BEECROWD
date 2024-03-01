import math

A = str(input())
B = str(input())

var = A.split(" ")
var2 = B.split(" ")


x1 = float(var.pop(1))
y1 = float(var.pop(0))

x2 = float(var2.pop(1))
y2 = float(var2.pop(0))

valor = ((x2 - x1)**2) + ((y2 - y1)**2)

print(f"{math.sqrt(valor):.4f}")