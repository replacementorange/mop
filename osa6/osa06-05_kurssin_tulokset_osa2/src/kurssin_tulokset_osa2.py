# tee ratkaisu tänne

# pyydetaan syote
opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedosto = input("Tehtävätiedot: ")
koepisteet = input("Koepisteet: ")

# luetaan opiskelijat tiedostosta
# opnro;etunimi;sukunimi
opiskelijat = {}

with open(opiskelijatiedot) as opiskelijatiedot_tiedosto:
    for rivi in opiskelijatiedot_tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            # jatetaan otsikkorivi huomioimatta
            continue
        opiskelijat[osat[0]] = f"{osat[1]} {osat[2].strip()}"

# luetaan tehtavat tiedostosta
# opnro;v1;v2;v3;v4;v5;v6;v7
tehtavat = {}

with open(tehtavatiedosto) as tehtavatiedosto_tiedosto:
    for rivi in tehtavatiedosto_tiedosto:
        osat = rivi.split(";")
        if osat[0] == "opnro":
            # jatetaan otsikkorivi huomioimatta
            continue
        # summa tehtaville
        summa = 0
        # lasketaan v1-v8 yhteen
        for i in range(1, 8):
            summa = summa + int(osat[i])
        # sijoitetaan summa tehtavien maaraksi
        tehtavat[osat[0]] = summa
        

# luetaan koepisteet tehtavasta
# opnro;k1;k2;k3
opiskelijan_koepisteet = {}

with open(koepisteet) as koepisteet_tiedosto:
    for rivi in koepisteet_tiedosto:
            osat = rivi.split(";")
            if osat[0] == "opnro":
            # jatetaan otsikkorivi huomioimatta
                continue
            # summa koepisteille
            summa = 0
            # lasketaan k1-k3 yhteen
            for i in range(1, 4):
                summa = summa + int(osat[i])
            # sijoitetaan summa tehtavien maaraksi
            opiskelijan_koepisteet[osat[0]] = summa

# lasketaan pisteet
def pisteet(piste_maara: int):
    return piste_maara // 4

# lasketaan arvosana
def arvosana(pisteet: int):
    arvosana = 0
    arvosana_rajat = [15, 18, 21, 24, 28]

    while arvosana < 5 and pisteet >= arvosana_rajat[arvosana]:
        arvosana = arvosana + 1
    return arvosana

# yhdistetaan tiedostojen tiedot yhteen tulostukseen
for opnro, nimi in opiskelijat.items():
    yhteensa = opiskelijan_koepisteet[opnro] + pisteet(tehtavat[opnro])
    print(f"{nimi} {arvosana(yhteensa)}")