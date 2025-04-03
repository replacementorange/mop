# Kirjoita ratkaisu tähän
# Otetaan käyttöön neliöjuuri math-moduulista
from math import sqrt

# Huomaa, että neliöjuuren voi laskea myös potenssin avulla:
# sqrt(9) on sama asia kuin 9 ** 0.5

a = int(input("Anna a: "))
b = int(input("Anna b: "))
c = int(input("Anna c: "))

d = (b**2) - (4*a*c)

pos_juuri = (-b-sqrt(d))/(2*a)  
neg_juuri = (-b+sqrt(d))/(2*a)  

print()
print(f"Juuret ovat {pos_juuri} ja {neg_juuri}")