m,n = list(map(int,input().split()))
a = str(m+n)

while a != "0":
    b = a
    for i in a: 
        if(i == "0"): b = a.replace("0","")
    print(b)
    m,n = list(map(int,input().split()))
    a  = str(m+n)

