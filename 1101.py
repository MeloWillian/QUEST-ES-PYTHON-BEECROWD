import io
buffer = io.StringIO()

l = list(map(int,(input().split())))
m = max(l)
p = min(l)

while m > 0 and p > 0:
    a=0
    for i in range(p,m+1):
            a+=i
            buffer.write(str(i) + " ")
    l = list(map(int,(input().split())))
    m = max(l)
    p = min(l)
    if(m > 0 and p > 0):buffer.write(f"Sum={str(a)}\n")
    else:buffer.write(f"Sum={str(a)}")
    
result = buffer.getvalue() 
print(result)   