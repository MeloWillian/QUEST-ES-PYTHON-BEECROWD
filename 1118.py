parcelado = 0
qtt = 0


while True:
    i = float(input())
    if(i >= 0 and i<=10):qtt+=1;parcelado+=i
    else:print("nota invalida")
    if(qtt==2):
        print(f"media = {(parcelado/2):.2f}")
        parcelado = 0
        qtt = 0
        print("novo calculo (1-sim 2-nao)")
        a = int(input())
        if a == 2:break
        while a != 1 and a != 2:
            print("novo calculo (1-sim 2-nao)")
            a = int(input())
            if a == 2:break
       
    