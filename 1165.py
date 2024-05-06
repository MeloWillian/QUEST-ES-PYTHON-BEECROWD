import math
v = int(input())

for i in range(v):
    value = int(input())
    if(value == 2 or value == 3 or value == 5 or value == 7):print(value,"eh primo")
    else:
        primo = True
        for i in range(2, math.isqrt(value) + 1):
            if value % i == 0:
                primo = False
                break
        if primo:
            print(value, "eh primo")
        else:
            print(value, "nao eh primo")
        

    