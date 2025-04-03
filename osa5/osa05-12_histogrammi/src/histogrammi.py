# tee ratkaisu tänne
def histogrammi(mjono: str):
    # alustetaan sanakirja
    sanakirja = {}
    # kaydaan lapi merkit merkkijonossa
    for merkki in mjono:
        # jos merkkia ei ole sanakirjassa
        if merkki not in sanakirja:
            # arvoksi 0
            sanakirja[merkki] = 0
        # jos merkki on sanakirjassa, arvo +1
        sanakirja[merkki] += 1
    # kaydaan lapi sanakirjassa olevat avain, arvo
    for avain, arvo in sanakirja.items():
        # tulostetaan avain ja esiintyman maara
        print(avain, "*" * arvo)

if __name__ == "__main__":
    print(histogrammi("abba"))