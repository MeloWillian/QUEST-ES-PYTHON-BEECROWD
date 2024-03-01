i,f = map(int,input().split())

if(i < f):
    j = f-i
    print(f"O JOGO DUROU {j} HORA(S)")
elif(f < i):
    j= (24-i)+f
    print(f"O JOGO DUROU {j} HORA(S)")
else: print("O JOGO DUROU 24 HORA(S)")


""" 
O JOGO PODE DURAR ENTRE 1 e 24 horas



"""