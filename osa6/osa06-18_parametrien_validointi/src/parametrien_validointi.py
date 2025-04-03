# tee ratkaisu tänne
def uusi_henkilo(nimi: str, ika: int):
    if not nimi:
        raise ValueError("nimi on tyhjä merkkijono")
    if len(nimi.split()) < 2:
        raise ValueError("nimi ei koostu vähintään kahdesta sanasta")
    if len(nimi) > 40:
        raise ValueError("nimen pituus on yli 40 merkkiä")
    if ika < 0:
        raise ValueError("ikä on negatiivinen luku")
    if ika > 150:
        raise ValueError("ikä on suurempi kuin 150")
    
    try:
        # luo henkilon
        henkilo = (nimi, ika)
    except ValueError as error:
        print(f"{error}")
    
    return henkilo
