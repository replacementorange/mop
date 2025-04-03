# tee ratkaisu tänne
# laskee matriisissa olevien summan
def summa():
    matriisi = lue_matriisi()
    return sum(sum(rivi) for rivi in matriisi)

# palauttaa matriisissa olevan suurimman arvon
def maksimi():
    matriisi = lue_matriisi()
    return max(max(rivi) for rivi in matriisi)

# palauttaa matrsiisissa olevien rivien summan
def rivisummat():
    matriisi = lue_matriisi()
    return [sum(rivi) for rivi in matriisi]

# lukee ja palauttaa matriisin .txt tiedostosta
def lue_matriisi():
    luettu_matriisi = []

    with open("matriisi.txt") as tiedosto:
        for rivi in tiedosto:
            numero = [int(numero) for numero in rivi.split(",")]
            luettu_matriisi.append(numero)
        return luettu_matriisi

if __name__ == "__main__":
    #print(lue_matriisi())
    print(summa())
    print(maksimi())
    print(rivisummat())