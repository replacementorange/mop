# tee ratkaisu tänne

# aloitetaan silmukka
while True:
    # syottee kysyminen
    print("1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu")
    syote = int(input("Valinta: "))

    # jos syote == 1
    # pyyda sanat fi ja en
    if syote == 1:
        # pyydetaan sanat
        fi = input("Anna sana suomeksi: ")
        en = input("Anna sana englanniksi: ")
        # kirjoitetaan sanat tiedostoon
        with open("sanakirja.txt", "a") as tiedosto:
            tiedosto.write(f"{fi} - {en}\n")
        # tulostetaan onnistumine
        print("Sanapari lisätty")

    # jos syote == 2
    # kysy haettavaa sana ja tulosta se jos on
    elif syote == 2:
        sana = str(input("Anna sana: "))
        with open("sanakirja.txt") as tiedosto:
            for rivi in tiedosto:
                rivi = rivi.replace("\n", "")
                # tulostetaan sana jos on sanakirjassa
                if sana in rivi:
                    print(rivi)

    # jos syote == 3
    # lopeta ohjelma
    elif syote == 3:
        print("Moi!")
        break