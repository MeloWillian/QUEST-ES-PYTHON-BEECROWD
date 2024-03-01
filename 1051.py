A = float(input())

if(A <= 2000):print("Isento")

elif(A > 2000 and A <=3000):
    b = A - 2000
    print(f"R$ {(b*0.08):.2f}")
    
elif(A > 3000 and A < 4500):
    b = A - 2000
    c = ((b // 1000) * 1000) * 0.08
    d = (b % 1000) * 0.18
    print(f"R$ {(c+d):.2f}")

else:
    a = 0.08 * 1000 
    c = 0.18 * 1500
    b = A - 4500
    d = (b * 0.28) 
    print(f"R$ {(d+c+a):.2f}")
    

