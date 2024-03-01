v1,v2,v3 = map(float, input().split())

if(v1 + v2 > v3 and v2 + v3 > v1 and v1 + v3 > v2 and v1>0 and v2>0 and v3>0):
    p = v1+v2+v3
    print(f"Perimetro = {p:.1f}")
else: 
    A = (   ((v1 + v2) * v3) / 2 )
    print(f"Area = {A:.1f}")

    