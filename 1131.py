grenais = 0
i = 0
g = 0
e = 0

while True:
    vi,vg = map(int, input().split())
    p = int(input())
    print("Novo grenal (1-sim 2-nao)")
    grenais +=1
    if(vi > vg): i+=1
    elif(vi < vg): g+=1
    else: e+=1
    if(p == 2):break
    
print(f"{grenais} grenais")
print(f"Inter:{i}")
print(f"Gremio:{g}")
print(f"Empates:{e}")

if(i > g):print("Inter venceu mais")
elif(g<i):print("Gremio venceu mais")
else:print("Nao houve vencedor")
    
    
