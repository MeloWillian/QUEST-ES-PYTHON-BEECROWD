v = int(input())
inn = 0
out = 0

for i in range(v):
    b = int(input())
    if(b >= 10 and b <= 20):inn+=1
    else:out+=1
    
print(inn, "in")
print(out, "out")
    