val = input()
l = val.split(" ")

t = [0, 4, 4.50, 5, 2, 1.50]

mult = int(l.pop(1))
a = int(l.pop(0))


v = t.pop(a)
print(f"Total: R$ {(v*mult):.2f}")