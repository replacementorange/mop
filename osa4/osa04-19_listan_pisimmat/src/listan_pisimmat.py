# tee ratkaisu tänne
def pisimmat(lista):
    # lista pisimmille
    pisimmat_sanat = []
    # etsitaan pisimmat sanat
    for sana in lista:
        # tarkista onko tyhja tai onko sana pidempi kuin listan pisin
        if not pisimmat_sanat or len(sana) > len(pisimmat_sanat[0]):
            # aseta sana
            pisimmat_sanat = [sana]
        # ellein jos sana yhtapitka kuin pisin
        elif len(sana) == len(pisimmat_sanat[0]):
            # lisaa sana
            pisimmat_sanat.append(sana)
    # palauta lista, TOIMI PLIIS.
    return pisimmat_sanat

if __name__ == "__main__":
    lista = ["eka", "toka", "kolmas", "seitsemäs"]
    tulos = pisimmat(lista)
    print(tulos) # ['seitsemäs']

    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]
    tulos = pisimmat(lista)
    print(tulos) # ['emilia', 'juhani']