# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(numero, merkki):
    if merkki == "":
        merkki = "*"
    elif len(merkki) > 1:
        merkki = merkki[0]
    print(merkki * numero)

def risulaatikko(korkeus):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    while korkeus > 0:
        viiva(10, "#")
        korkeus -= 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risulaatikko(5)
    print()
    risulaatikko(2)
