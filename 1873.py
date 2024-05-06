n = int(input())

for i in range(n):
    raj,shel = input().split()
    if(raj == shel):print("empate")
    else:
        if(raj == "tesoura" and (shel == "lagarto" or shel == "papel")):print("rajesh")
        elif(raj == "papel" and (shel == "spock" or shel == "pedra")):print("rajesh")
        elif(raj == "pedra" and (shel == "tesoura" or shel == "largato")):print("rajesh")
        elif(raj == "lagarto" and (shel == "spock" or shel == "papel")):print("rajesh")
        elif(raj == "spock" and (shel == "pedra" or shel == "tesoura")):print("rajesh")
        else:print("sheldon")
       
    
