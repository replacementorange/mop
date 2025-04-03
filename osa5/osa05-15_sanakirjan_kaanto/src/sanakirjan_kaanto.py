# tee ratkaisu tänne
def kaanna(sanakirja: dict):
    # Sanakirja kopiota varten
    sanakirjan_kopio = {}

    # Kaydaan sanakirjan avaimen lapi
    for avain in sanakirja:
        # Kopiodaan
        sanakirjan_kopio[avain] = sanakirja[avain]

    # Tyhjennetaan sanakirja
    for avain in sanakirjan_kopio:
        # Poistaa avaimen
        del sanakirja[avain]

    # Kopiodaan alkuperaiseen kaantaen
    for avain in sanakirjan_kopio:
        sanakirja[sanakirjan_kopio[avain]] = avain

if __name__ == "__main__":
    s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
    kaanna(s)
    print(s)