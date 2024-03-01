a,b = map(int, input().split())
import math

if(math.gcd(a,b) == a or math.gcd(a,b) == b ): print("Sao Multiplos")
else: print("Nao sao Multiplos")

