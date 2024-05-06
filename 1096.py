qtt = 0
C = 0
R = 0
S = 0

n = int(input())
for i in range(n):
    nu,t = input().split()
    nu = int(nu)

    qtt+=nu
    if(t == "C"): C+=nu
    elif(t == "S"): S+=nu
    elif(t == "R"): R+=nu

pC = (f"{((100*C) / qtt):.2f}")
pR = (f"{((100*R) / qtt):.2f}")
pS = (f"{((100*S) / qtt):.2f}")

print(f"Total: {qtt} cobaias")
print(f"Total de coelhos: {C}")
print(f"Total de ratos: {R}")
print(f"Total de sapos: {S}")
print(f"Percentual de coelhos: {pC} %")
print(f"Percentual de ratos: {pR} %")
print(f"Percentual de sapos: {pS} %")