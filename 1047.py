i,im,f,fm = map(int,input().split())


if(i < f and fm > im):
    j = f-i
    p = fm - im
    print(f"O JOGO DUROU {j} HORA(S) E {p} MINUTO(S)")
  
elif(f < i and fm < im):
    j= ((24-i) +f) - 1
    p = fm - im
    print(f"O JOGO DUROU {j} HORA(S) E {60+p} MINUTO(S)")
    
elif(f == i and fm < im):
    p = fm - im
    print(f"O JOGO DUROU {23} HORA(S) E {60+p} MINUTO(S)")
    
elif(f > i and fm < im):
    j= (f-i) - 1
    p = fm - im
    
    print(f"O JOGO DUROU {j} HORA(S) E {60+p} MINUTO(S)")
    
elif(i == f and im < fm):
    
    print(f"O JOGO DUROU 0 HORA(S) E {fm-im} MINUTO(S)")
    
elif(i == im and i == f and i== fm): print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

