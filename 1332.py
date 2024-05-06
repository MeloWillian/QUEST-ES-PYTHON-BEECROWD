n = int(input())
for i in range(n):
    p = input()
    if(len(p) == 5):print(3)
    else:
        if(all(l in p for l in ["n"])):
            if(p[0] == "o" or p[2] == "e"):print("1")
        elif(p[0] == "o" and p[2] == "e"):print("1")
        if(all(l in p for l in ["w"])):
            if(p[0] == "t" or p[2] == "o"):print("2")
        elif(p[0] == "t" and p[2] == "o"):print("2")
    