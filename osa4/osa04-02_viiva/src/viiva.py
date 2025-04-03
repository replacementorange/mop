# tee ratkaisu tänne
def viiva(numero, merkki):
    if merkki == "":
        merkki = "*"
    elif len(merkki) > 1:
        merkki = merkki[0]
    print(merkki * numero)

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    viiva(5, "x")
    viiva(3, "")
