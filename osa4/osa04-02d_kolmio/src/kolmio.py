# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(numero, merkki):
    if merkki == "":
        merkki = "*"
    elif len(merkki) > 1:
        merkki = merkki[0]
    print(merkki * numero)

def kolmio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    leveys = 1
    while leveys <= koko:
        viiva(leveys, "#")
        leveys += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kolmio(6)
    print()
    kolmio(3)
