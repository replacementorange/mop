mjono = input("Sana: ")
merkki = input("Merkki: ")

while True:
    kohta = mjono.find(merkki)
    if kohta >= 0:
        loydetyt = mjono[kohta:kohta + 3]
        if len(loydetyt) < 3:
            print()
            break
        else:
            print(f"{loydetyt}")
            mjono = mjono[kohta + 1:]
    else:
        break