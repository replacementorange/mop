luku1 = int(input("Luku 1: "))
luku2 = int(input("Luku 2: "))

komento = str(input("Komento: "))

if (komento == "summa"):
    print()
    print(f"{luku1} + {luku2} = {luku1+luku2}")
elif (komento == "erotus" ):
    print()
    print(f"{luku1} - {luku2} = {luku1-luku2}")
elif (komento == "tulo"):
    print()
    print(f"{luku1} * {luku2} = {luku1*luku2}")
else:
    print("")