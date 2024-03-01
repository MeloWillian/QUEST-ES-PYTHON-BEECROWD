lista = input()
listaSep = lista.split(" ")

C = float(listaSep.pop(2))
B = float(listaSep.pop(1))
A = float(listaSep.pop(0))

a = (A * C)/ 2
b = (C**2) * 3.14159
c = ((A + B) * C) / 2
d = B**2
e = A * B


print(f"TRIANGULO: {a:.3f}")
print(f"CIRCULO: {b:.3f}")
print(f"TRAPEZIO: {c:.3f}")
print(f"QUADRADO: {d:.3f}")
print(f"RETANGULO: {e:.3f}")