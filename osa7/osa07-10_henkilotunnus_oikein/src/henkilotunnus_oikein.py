# tee ratkaisu tänne

from datetime import datetime

# https://dvv.fi/henkilotunnus
# Ohjelman tulee tarkastaa, että
# alkuosassa on ppkkvv-muodossa oleva päivämäärä, joka on olemassa oleva päivämäärä
# välimerkki on + (1800-luku), - (1900-luku) tai A (2000-luku) ja
# lopussa oleva tarkastusmerkki on oikein.

def onko_validi(hetu: str):
    # tarkistetaan pituus
    if len(hetu) != 11:
        return False

    # poimitaan numerot ja tarkistetaan ne
    # ppkkvvXyyyz
    numerot = hetu[:6] + hetu[7:10]
    for n in numerot:
        if n not in numerot:
            return False
    
    # katsotaan valimerkki ([6]) ja tarkistetaan, etta on sallittu + - A
    valimerkki = hetu[6]
    if valimerkki not in "+-A":
        return False
    
    # maaritellaan paiva, kuukausi ja vuosi
    # ppkkvvXyyyz
    pp = int(hetu[0:2])
    kk = int(hetu[2:4])
    vv = int(hetu[4:6])

    # paatellaan syntymatuhannes merkin avulla (+ 1800, - 1900, A 2000)
    if valimerkki == "+":
        vv = vv + 1800
    if valimerkki == "-":
        vv = vv + 1900
    if valimerkki == "A":
        vv = vv + 2000
    
    # kokeillaan muodostaa paivays
    try:
        paivays = datetime(vv, kk, pp)
    except:
        return False
    
    merkki_jono = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    # 31
    numerosarja = int(numerot) % 31

    return merkki_jono[numerosarja] == hetu[-1]
    

    

if __name__ == "__main__":
    print(onko_validi("230827-906F"))
    print(onko_validi("20488+246L"))
    print(onko_validi("310823A9877"))
    print()

