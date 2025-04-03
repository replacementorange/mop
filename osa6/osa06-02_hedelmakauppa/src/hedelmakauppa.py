# tee ratkaisu tänne
def lue_hedelmat():
    hedelma_sanakirja = {}
    with open("hedelmat.csv") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            osat = rivi.split(";")
            hedelma = osat[0]
            hinta = osat[1]
            hedelma_sanakirja[hedelma] = float(hinta)
    return hedelma_sanakirja

if __name__ == "__main__":
    print(lue_hedelmat())