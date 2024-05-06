l = [6,2,5,5,4,5,6,3,7,6]
b = int(input())

# for p in range(b): 

while b != 0:
    a = input()
    valor = 0
    for i in a:
            valor += l[int(i)]
    print(valor)
    b-=1