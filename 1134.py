program = 0
a = 0
g = 0
d = 0
while program != 4:
    v = int(input())
    if(v == 1): a+=1
    elif(v == 2): g+=1
    elif(v == 3): d+=1
    program = v

print("MUITO OBRIGADO")
print(f"Alcool: {a}")
print(f"Gasolina: {g}")
print(f"Diesel: {d}")


