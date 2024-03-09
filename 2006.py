A = int(input())
l = list(map(int,input().split()))
c= 0

for i in l:
    if(i == A):c+=1

print(c)
