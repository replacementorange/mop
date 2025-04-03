# tee ratkaisu tänne
# sanakirja puh.luettoloa varten
puhelinluettelo = {}

while True:
    syote = int(input("komento (1 hae, 2 lisää, 3 lopeta): "))
    
    if syote == 1:
        # kysytaan nimi
        nimi = str(input("nimi: "))
        # jos nimi on sanakirjassa
        if nimi in puhelinluettelo:
            # tulostetaan nimi
            print(puhelinluettelo[nimi])
        else:
            print("ei numeroa")
    elif syote == 2:
        # kysytaan nimi ja nro
        nimi = str(input("nimi: "))
        numero = str(input("numero: "))
        # lisataan sanakirjaan
        puhelinluettelo[nimi] = numero
        print("ok!")
    elif syote == 3:
        print("lopetetaan...")
        break