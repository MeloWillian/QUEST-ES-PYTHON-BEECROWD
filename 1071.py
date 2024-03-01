A = int(input())
B = int(input())
l= []
s = 0

if(A !=  B):
    if(A > B): 
        while (A > B):
         A -= 1
         if(A > B and A % 2 != 0): l.append(A)

    elif(A < B): 
        while (A < B):
         B -= 1
         if(A < B and B % 2 != 0): l.append(B)

    else: print(0)

    for i in l:
        s += i  
    print(s)
    
else: print(0)

    
   

    
