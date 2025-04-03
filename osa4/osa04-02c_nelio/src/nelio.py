# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(numero, merkki):
    if merkki == "":
        merkki = "*"
    elif len(merkki) > 1:
        merkki = merkki[0]
    print(merkki * numero)

def nelio(koko, merkki):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    #viiva(4, merkki)

    kerta = koko
    while kerta > 0:
        viiva(koko, merkki)
        kerta -= 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    nelio(5, "*")
    print()
    nelio(3, "o")
