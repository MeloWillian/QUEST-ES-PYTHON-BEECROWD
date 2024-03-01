l = list(map(float, input().split()))

media = ((l[0] * 2) + (l[1]*3) + (l[2] * 4) + (l[3] * 1)) / 10

print("Media:", round(media,1))
if(media >= 7.0): print("Aluno aprovado.")

elif(media >= 5.0 and media <= 6.9): 
    print("Aluno em exame.")
    a= float(input()) 
    print("Nota do exame:",a)
    mf = ((media + a)/2)
    if( mf >= 5):print("Aluno aprovado.")
    else: print("Aluno reprovado.")
    print(f"Media final: {mf:.1f}")
    
else: print("Aluno reprovado.")

