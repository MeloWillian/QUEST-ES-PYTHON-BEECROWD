par=0
impar = 0
posi = 0
neg = 0

for i in range(5):
    A = int(input())
    if A % 2 == 0: par+=1
    if A % 2 != 0: impar+=1
    if A > 0: posi+=1
    if A < 0: neg+=1 

    
print(par, "valor(es) par(es)")
print(impar, "valor(es) impar(es)")
print(posi, "valor(es) positivo(s)")
print(neg,"valor(es) negativo(s)")