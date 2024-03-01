A = str(input())

var = A.split(" ")

p = int(var.pop(0))
k = int(var.pop(0))



val = k/(p+2)

print(f"{val:.2f}")