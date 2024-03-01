a = float(input())

if(a >= 0 and a <=400):
    n = (a * 0.15) + a
    r = a * 0.15
    p = 15

    print(f"Novo salario: {n:.2f}")
    print(f"Reajuste ganho: {r:.2f}")
    print(f"Em percentual: {p} %")

elif(a > 400 and a <=800):
     n = (a * 0.12) + a
     r= a * 0.12
     p = 12
     print(f"Novo salario: {n:.2f}")
     print(f"Reajuste ganho: {r:.2f}")
     print(f"Em percentual: {p} %")

elif(a > 800 and a <=1200):
     n = (a * 0.10) + a
     r= a * 0.10
     p = 10

     print(f"Novo salario: {n:.2f}")
     print(f"Reajuste ganho: {r:.2f}")
     print(f"Em percentual: {p} %")
elif(a > 1200 and a <=2000):
     n = (a * 0.07) + a
     r= a * 0.07
     p = 7

     print(f"Novo salario: {n:.2f}")
     print(f"Reajuste ganho: {r:.2f}")
     print(f"Em percentual: {p} %")
elif(a > 2000):
     n = (a * 0.04) + a
     r= a * 0.04
     p = 4
     
     print(f"Novo salario: {n:.2f}")
     print(f"Reajuste ganho: {r:.2f}")
     print(f"Em percentual: {p} %")

""" 

15%
12%
10%
7%
4%
0 - 400.00              
400.01 - 800.00
800.01 - 1200.00
1200.01 - 2000.00
Acima de 2000.00 
"""
