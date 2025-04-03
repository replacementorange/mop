# tee ratkaisu tänne
def suodata_laskut():
    # luetaan .csv
    with open('laskut.csv', 'r') as laskut:
        rivit = laskut.readlines()

    # oikeat laskut --> oikeat.csv
    oikeat_laskut = []
    # vaarat laskut --> vaarat.csv
    vaarat_laskut = []

    # kaydaan lapi rivit
    for rivi in rivit:
        nimi, lasku, tulos = rivi.strip().split(';')
        # etsitaan ja erotatan operandit (kato 7. osioo)
        operandit = lasku.split('+') if '+' in lasku else lasku.split('-')
        operandi1, operandi2 = map(int, operandit)
        lasku = operandi1 + operandi2 if '+' in lasku else operandi1 - operandi2

        # tarkistetaan onko lasku oikein ja lisataan se listaan
        if int(tulos) == lasku:
            oikeat_laskut.append(rivi)
        else:
            vaarat_laskut.append(rivi)
    
    # kirjoitetaan oikeat tiedostoon
    with open('oikeat.csv', 'w') as oikeat_tiedosto:
        oikeat_tiedosto.writelines(oikeat_laskut)
    # kirjoitetaan vaarat tiedostoon
    with open('vaarat.csv', 'w') as vaarat_tiedosto:
        vaarat_tiedosto.writelines(vaarat_laskut)

if __name__ == "__main__":
    suodata_laskut()