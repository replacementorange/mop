nimi = str(input("Mikä on nimesi: "))
keitto = float(5.90)

if (nimi == "Jerry"): #  
    print("Seuraava!")
else:
    maara = int(input("Kuinka monta annosta keittoa: "))
    print(f"Kokonaishinta on {keitto * maara}")
    print("Seuraava!")