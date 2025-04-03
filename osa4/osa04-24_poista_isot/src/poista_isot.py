# tee ratkaisu tänne
def poista_isot(lista):
    pieni_lista = []
    for sana in lista:
        if not sana.isupper():
            pieni_lista.append(sana)
    return pieni_lista

if __name__ == "__main__":
    lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
    karsittu_lista = poista_isot(lista)
    print(karsittu_lista)