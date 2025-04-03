# tee ratkaisu tänne
def hae_sanat(hakusana: str):
    # luetaan tiedosto
    with open('sanat.txt', 'r') as tiedosto:
        sanat = tiedosto.read().splitlines()
    
    loydetyt = []

    # tarkistetaan tahti alussa ja lopussa
    if "*" in hakusana:
        if hakusana.startswith("*"):
            for sana in sanat:
                if sana.endswith(hakusana[1:]):
                    loydetyt.append(sana)
        elif hakusana.endswith("*"):
            for sana in sanat:
                if sana.startswith(hakusana[:-1]):
                    loydetyt.append(sana)

    # tarkistetaan piste
    if "." in hakusana:
        for sana in sanat:
            if len(sana) == len(hakusana):
                loytyi = True
                for i in range(len(sana)):
                    if hakusana[i] != "." and hakusana[i] != sana[i]:
                        loytyi = False
                        break
                if loytyi:
                    loydetyt.append(sana)

    # muut tapahtumat --> etsitaan sanat
    else:
        for sana in sanat:
            if sana == hakusana:
                loydetyt.append(sana)

    return loydetyt

if __name__ == "__main__":
    print(hae_sanat("*vokes")) # ['convokes', 'equivokes', 'evokes', 'invokes', 'provokes', 'reinvokes', 'revokes']
    print(hae_sanat("cat"))