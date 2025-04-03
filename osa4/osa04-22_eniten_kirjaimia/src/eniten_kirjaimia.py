# tee ratkaisu tänne
def eniten_kirjainta(mjono: str):
    # asetetaan eka yleisimmaks
    eniten = mjono[0]

    # kaydaan kirjaimet yleisyys
    for merkki in mjono:
        # jos kirjainta esiintyy enemman niin se on uusi eniten
        if mjono.count(eniten) < mjono.count(merkki):
            eniten = merkki

    return eniten

if __name__ == "__main__":
    mjono = "abcbdbe"
    print(eniten_kirjainta(mjono)) # b

    toinen_jono = "esimerkkimerkkijonokki"
    print(eniten_kirjainta(toinen_jono)) # k