# tee ratkaisu tänne
nimi = str(input("Kenelle teos omistetaan: "))
tiedosto = str(input("Mihin kirjoitetaan: "))

with open(tiedosto, "w") as kirjoitettava:
    kirjoitettava.write(f"Hei {nimi}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi")