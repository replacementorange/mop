mjono = input("Sana: ")
merkki = input("Merkki: ")

kohta = mjono.find(merkki)
if kohta >= 0:
    loydetyt = mjono[kohta:kohta + 3]
    if len(loydetyt) < 3:
        print()
    else:
        print(f"{loydetyt}")
else:
    print()