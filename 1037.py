""" Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem 
dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este
valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos, 
deverá ser impressa a mensagem “Fora de intervalo”.
 """
 
A = float(input())
l = ["0,25", "25,50", "50,75", "75,100"]

if(A >= 0 and A <= 100):
    if(A >= 0 and A <=25): print(f"Intervalo [0,25]")
    elif(A > 25 and A <= 50):print(f"Intervalo (25,50]")
    elif(A > 50 and A <= 75):print(f"Intervalo (50,75]")
    elif(A > 75 and A <= 100):print(f"Intervalo (75,100]")
else: print("Fora de intervalo")






""" def teste (t,val1,val2): 
    
    if(t >= 0 and t <= 25): print(f"Intervalo [0,25]"); 
    else: print(f"Intervalo ({val1},{val2}]")
    
   

if(A >= 0 and A <= 100):
    for i in l: 
        b = i.split(",")
        teste(A,b.pop(0),b.pop(0)) """
      

    
    
