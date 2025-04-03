# tee ratkaisu tänne
def hae_nimi(tiedosto: str, sana: str):
    loydetyt_reseptit = []
    # avataan tiedosto
    with open(tiedosto, "r") as tiedosto:
        resepti = []
        for rivi in tiedosto:
            rivi = rivi.strip()
            if not rivi:
                if resepti and sana.lower() in resepti[0].lower():
                    loydetyt_reseptit.append(resepti[0])
                resepti = []
            else:
                resepti.append(rivi)

        if resepti and sana.lower() in resepti[0].lower():
            loydetyt_reseptit.append(resepti[0])

    return loydetyt_reseptit

def hae_aika(tiedosto, aika):
    reseptit = []
    ajat = []
    with open(tiedosto) as tiedosto:
        sisalto = tiedosto.read()
        sisalto = sisalto.split("\n\n")
        for alkio in sisalto:
            alkio = alkio.split("\n")
            reseptit.append(alkio)
        for resepti in reseptit:
            if int(resepti[1]) <= aika:
                ajat.append((f"{resepti[0]}, valmistusaika {resepti[1]} min"))
    return ajat

def hae_raakaaine(tiedosto: str, aine: str):
    reseptit = []
    ainesosat = []
    with open(tiedosto) as tiedosto:
        sisalto = tiedosto.read()
        sisalto = sisalto.split("\n\n")

        for alkio in sisalto:
            alkio = alkio.split("\n")
            reseptit.append(alkio)

        for resepti in reseptit:
            if aine in resepti[2:]:
                ainesosat.append((f"{resepti[0]}, valmistusaika {resepti[1]} min"))
                
    return ainesosat

if __name__ == "__main__":
    loydetyt = hae_nimi("reseptit1.txt", "pulla")
    for resepti in loydetyt:
        print(resepti)

    loydetyt = hae_aika("reseptit1.txt", 20)

    for resepti in loydetyt:
        print(resepti)

    loydetyt = hae_raakaaine("reseptit1.txt", "maito")

    for resepti in loydetyt:
        print(resepti)