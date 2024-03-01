list = map(float,input().split())
A,B,C = sorted(list, reverse = True)


if(A < B+C):
    
    if ((A**2) == ((B**2) + (C**2))): print("TRIANGULO RETANGULO")
    elif ((A**2) > ((B**2) + (C**2))): print("TRIANGULO OBTUSANGULO")
    elif ((A**2) < ((B**2) + (C**2))): print("TRIANGULO ACUTANGULO")

    if(A == B and B == C and C == A): print("TRIANGULO EQUILATERO")
    elif(A==B and B != C or B==C and A != B): print("TRIANGULO ISOSCELES")
    
else: print("NAO FORMA TRIANGULO")