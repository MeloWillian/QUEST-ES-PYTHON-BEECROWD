l = int(input())
s = input()
somador = 0
matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)        

for el in matriz[l]:
    somador += el

if(s == "S"):
    print(f"{(somador):.1f}")
elif(s == "M"):  print(f"{(somador/12):.1f}")