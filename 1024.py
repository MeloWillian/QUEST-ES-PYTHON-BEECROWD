resultados = []
A= int(input())


for i in range(A):

    texto = str(input())
    valores_ascii = []

    for i in texto:
        if ord(i) >= 65 and ord(i)<=90:valores_ascii.append(chr(ord(i)+3))
        elif ord(i) >= 97 and ord(i)<=122:valores_ascii.append(chr(ord(i)+3))
        else:valores_ascii.append(i)

    sec = valores_ascii[::-1]
    tmn = int(len(sec))
    tmn2 = tmn // 2

    while tmn2 < tmn:
        sec[tmn2] =  chr(ord(sec[tmn2])-1)
        tmn2 +=1

    resultados.append(''.join(sec)) 


for i in resultados: print(i)
