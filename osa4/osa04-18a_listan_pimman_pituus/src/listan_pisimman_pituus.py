# tee ratkaisu tänne
def pisimman_pituus(lista):
    paras = lista[0]
    for alkio in lista:
        if len(alkio) >= len(paras):
            paras = alkio
    return len(paras)

if __name__ == "__main__":
    lista = ["eka", "toka", "kolmas", "seitsemäs"]
    tulos = pisimman_pituus(lista)
    print(tulos)

    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]
    tulos = pisimman_pituus(lista)
    print(tulos)