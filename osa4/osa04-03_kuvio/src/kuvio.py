# kopioi edellisestä tehtävästä funktion viiva koodi tänne, ja toteuta funktio kuvio sitä hyödyntäen
def viiva(numero, merkki):
    if merkki == "":
        merkki = "*"
    elif len(merkki) > 1:
        merkki = merkki[0]
    print(merkki * numero)


def kuvio(num1, char1, num2, char2):
    # Pyramidi
    leveys = 1
    while leveys <= num1:
        viiva(leveys, char1)
        leveys += 1
    # Viiva
    pituus = num2
    while pituus > 0:
        viiva(num1, char2)
        pituus -= 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kuvio(5, "X", 3, "*")
    print()
    kuvio(2, "o", 4, "+")
    print()
    kuvio(3, ".", 0, ",")
    print()
    kuvio(5, "X", 3, "*")
