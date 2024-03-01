A = int(input())

horas = 0
minutos = int(A / 60)
segundosSobra = int(A % 60 )

if(minutos >= 60): 
  while minutos >= 60: horas +=1; minutos -= 60



print(f"{horas}:{minutos}:{segundosSobra}")