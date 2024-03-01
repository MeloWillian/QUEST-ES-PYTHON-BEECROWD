A = input()

val = A.split(" ")
maior = 0



for i in val: 
  if(int(i) >= int(maior)): maior = i


print(f"{maior} eh o maior") 