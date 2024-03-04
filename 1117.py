n = 0
v = 0

while n != 2 :
    b= float(input())
    if(b <= 10 and b >=0): v+=b; n+=1
    else: print("nota invalida")
        
print(f"media = {(v/2):.2f}")
    