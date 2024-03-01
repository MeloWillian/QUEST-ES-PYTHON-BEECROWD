""" Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D 
for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, 
ambos, forem positivos e se a variável A for par escrever a mensagem 
"Valores aceitos", senão escrever "Valores nao aceitos". """

A = input()
l = A.split(" ")

if(int(l[1]) > int(l[2]) and int(l[3]) > int(l[0]) and (int(l[2]) + int(l[3]))  > (int(l[0]) + int(l[1])) and int(l[2]) > 0 and int(l[3]) > 0 and int(l[0]) % 2 == 0): 
    print("Valores aceitos")	

else:print("Valores nao aceitos")
