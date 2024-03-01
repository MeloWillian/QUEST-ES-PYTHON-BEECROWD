A = int(input())

anos = 0
meses = 0
dias = 0


# while(dias <= 0):
if(A >= 365): 
    while A >= 365: anos +=1; A -= 365
if(A<365 and A>=30): meses = int(A / 30); dias = int(A % 30)
else: A = dias
      

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")