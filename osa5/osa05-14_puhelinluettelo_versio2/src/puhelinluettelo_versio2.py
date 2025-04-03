# tee ratkaisu tänne

# Haetaan henkilot
def hae(henkilot):
    nimi = input("nimi: ")
    if nimi in henkilot:
        for numero in henkilot[nimi]:
            print(numero)
    else:
        print("ei numeroa")

# Lisataan henkilot
def lisaa(henkilot):
    nimi = input("nimi: ")
    numero = input("numero: ")

    if nimi not in henkilot:
        henkilot[nimi] = []
    henkilot[nimi].append(numero)
    print("ok!")
    
# Paaohjelma
def main():
    henkilot = {}
    while True:
        komento = input("komento (1 hae, 2 lisää, 3 lopeta): ")
        if (komento == "1"):
            hae(henkilot)
        if (komento == "2"):
            lisaa(henkilot)
        if (komento == "3"):
            break
    print("lopetetaan...")

main()