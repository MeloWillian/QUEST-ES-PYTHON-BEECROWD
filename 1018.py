A = float(input())
cons = A


cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0

while A > 0:
  if(A >= 100):
    value = A / 100
    A -= 100*int(value)
    cem += int(value)
  elif(A >= 50):
    value = A / 50
    A -= 50*int(value)
    cinquenta += int(value)
  elif(A >= 20):
    value = A / 20
    A -= 20*int(value)
    vinte += int(value)
  elif(A >= 10):
    value = A / 10
    A -= 10*int(value)
    dez += int(value)
  elif(A >= 5):
    value = A / 5
    A -= 5*int(value)
    cinco += int(value)
  elif(A >= 2):
    value = A / 2
    A -= 2*int(value)
    dois += int(value)
  elif(A >= 1):
    value = A / 1
    A -= 1*int(value)
    um += int(value)



print(int(cons))
print(f"{cem} nota(s) de R$ 100,00")
print(f"{cinquenta} nota(s) de R$ 50,00")
print(f"{vinte} nota(s) de R$ 20,00")
print(f"{dez} nota(s) de R$ 10,00")
print(f"{cinco} nota(s) de R$ 5,00")
print(f"{dois} nota(s) de R$ 2,00")
print(f"{um} nota(s) de R$ 1,00")