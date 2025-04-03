# tee ratkaisu tänne
while True:
    print(f"1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta")
    syote = input("Valinta: ")
    if syote == "1":
        merkinta = input("Anna merkintä: ")
        with open("paivakirja.txt", "a") as tiedosto:
            tiedosto.write(merkinta + "\n")
        print("Päiväkirja tallennettu")
    elif syote == "2":
        with open("paivakirja.txt") as tiedosto:
            sisalto = tiedosto.read()
            print("Merkinnät: ")
            print(sisalto)
    elif syote == "0":
        print("Heippa!")
        break