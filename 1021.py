valor = float(input()) * 100
valores = [100,50,20,10,5,2,1,0.50,0.25,0.10,0.05,0.01]
lista = []
cons = valor

for i in valores: lista.append(int(valor // (i*100))); valor %= (i*100)

print("NOTAS:")
print(f"{lista[0]} nota(s) de R$ 100.00")
print(f"{lista[1]} nota(s) de R$ 50.00")
print(f"{lista[2]} nota(s) de R$ 20.00")
print(f"{lista[3]} nota(s) de R$ 10.00")
print(f"{lista[4]} nota(s) de R$ 5.00")
print(f"{lista[5]} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{lista[6]} moeda(s) de R$ 1.00")
print(f"{lista[7]} moeda(s) de R$ 0.50")
print(f"{lista[8]} moeda(s) de R$ 0.25")
print(f"{lista[9]} moeda(s) de R$ 0.10")
print(f"{lista[10]} moeda(s) de R$ 0.05")
print(f"{lista[11]} moeda(s) de R$ 0.01") 