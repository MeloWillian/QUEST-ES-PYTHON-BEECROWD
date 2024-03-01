
var = int(input())

import math
i = 0
l = []

def reduzir(numerador, denominador):
    a = int(numerador) / int(math.gcd(numerador,denominador))
    b = int(denominador) / int(math.gcd(numerador,denominador))
    return(f"{int(a)}/{int(b)}")

for i in range(var):
    a=input() 
    t = a.split(" ")
    d2 = int(t[6])
    n2 = int(t[4])
    b = t[3]
    d1 = int(t[2])
    n1 = int(t[0])

    if b == "+":
      numerador = (n1*d2) + (n2*d1)  
      denominador = d1*d2
      l.append(f"{numerador}/{denominador} = {reduzir(numerador,denominador)}")

    elif b == "-":  
      numerador = (n1*d2) - (n2*d1)
      denominador = d1*d2
      l.append(f"{numerador}/{denominador} = {reduzir(numerador,denominador)}")
    
    elif b == "*":
       numerador = int(n1*n2)
       denominador = int(d2*d1)
       gcd = int(math.gcd(numerador,denominador))
       l.append(f"{numerador}/{denominador} = {int(numerador/gcd)}/{int(denominador/gcd)}")
    elif b == "/": 
        numerador = int(n1*d2)
        denominador = int(n2*d1)
        gcd = int(math.gcd(numerador,denominador))
        l.append(f"{numerador}/{denominador} = {int(numerador/gcd)}/{int(denominador/gcd)}")

for i in l: print(i) 



