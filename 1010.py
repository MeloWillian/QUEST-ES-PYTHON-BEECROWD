A = str(input())
B = str(input())


lista1 = A.split(" ")
lista2 = B.split(" ")

val1 = float(lista1.pop(2)) * float(lista1.pop(1))

val2 = float(lista2.pop(2)) * float(lista2.pop(1)) 


print(f"VALOR A PAGAR: R$ {(val1 + val2):.2f}")