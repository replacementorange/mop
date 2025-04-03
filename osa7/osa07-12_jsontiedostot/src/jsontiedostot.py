# tee ratkaisu tänne
import json

def tulosta_henkilot(tiedosto: str):
    with open(tiedosto) as tiedosto:
        data = tiedosto.read()
    kurssit = json.loads(data)
    for kurssi in kurssit:
        harrastukset = ", ".join(kurssi["harrastukset"])
        print(kurssi["nimi"], kurssi["ika"], 'vuotta (' + harrastukset + ')')

if __name__ == "__main__":
    tulosta_henkilot("tiedosto1.json")
    tulosta_henkilot("tiedosto2.json")
    tulosta_henkilot("tiedosto3.json")
    tulosta_henkilot("tiedosto4.json")