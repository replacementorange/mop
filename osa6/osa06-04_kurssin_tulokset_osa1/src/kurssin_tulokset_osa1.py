# tee ratkaisu tänne
if True:
    # tänne ei tulla
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
else:
    # kovakoodatut syötteet
    opiskelijatiedot = "opiskelijat1.csv"
    tehtavatiedot = "tehtavat1.csv"

nimet = {}

with open(opiskelijatiedot) as opiskelija_tiedosto:
    for rivi in opiskelija_tiedosto:
        osat = rivi.split(';')
        if osat[0] == "opnro":
            continue
        nimet[osat[0]] = osat[1].strip() + " " + osat[2].strip()

tehtavat = {}

with open(tehtavatiedot) as tehtava_tiedosto:
    for rivi in tehtava_tiedosto:
        osat = rivi.split(';')
        if osat[0] == "opnro":
            continue
        tehtavat[osat[0]] = int(osat[1]) + int(osat[2]) + int(osat[3]) + int(osat[4]) + int(osat[5]) + int(osat[6]) + int(osat[7])

for opnro, etunimi in nimet.items():
    if opnro in tehtavat:
        tehtava = tehtavat[opnro]
        print(f"{etunimi} {tehtava}")
    else:
        print(f"{etunimi} - Ei oo")