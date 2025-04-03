# tee ratkaisu tänne
import csv
from datetime import datetime, timedelta

def huijarit():
    # luetaan palautukset
    with open("tentin_aloitus.csv") as aloitus, open("palautus.csv") as palautus:

        # ajat
        aloitusajat = {}
        palautusajat = {}

        # huijarit
        huijarit = []

        # haetaan aloitusajat
        # muoto: matti;13:33 | tunnus;hh:mm
        for rivi in csv.reader(aloitus, delimiter=";"):
            nimi = rivi[0]
            aika_aloitus = datetime.strptime(rivi[1], "%H:%M")
            aloitusajat[nimi] = aika_aloitus

        # haetaan palautusajat
        for rivi in csv.reader(palautus, delimiter=";"):
            nimi = rivi[0]
            aika_palautus = datetime.strptime(rivi[3], "%H:%M")

            # jos ei loydy niin lisataan
            if nimi not in palautusajat:
                palautusajat[nimi] = aika_palautus
            # jos loytyy niin verrataan
            elif aika_palautus > palautusajat[nimi]:
                palautusajat[nimi] = aika_palautus

        # poimitaan huijarit
        # https://docs.python.org/3/library/datetime.html#timedelta-objects
        for nimi in aloitusajat:
            if (palautusajat[nimi] - aloitusajat[nimi]) > timedelta(hours = 3):
                huijarit.append(nimi)
        
        return huijarit
            

if __name__ == "__main__":
    print(huijarit())