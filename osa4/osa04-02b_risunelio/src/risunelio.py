# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(numero, merkki):
    if merkki == "":
        merkki = "*"
    elif len(merkki) > 1:
        merkki = merkki[0]
    print(merkki * numero)

def risunelio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    kerta = koko
    while kerta > 0:
        viiva(koko, "#")
        kerta -= 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)
    print()
    risunelio(3)
