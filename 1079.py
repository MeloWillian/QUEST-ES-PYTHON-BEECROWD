cont = int(input())

for i in range(cont):
    med = 0
    a,b,c = map(float,input().split())
    med+= a*2
    med+= b*3
    med+= c*5
    print(f"{(med/10):.1f}")
