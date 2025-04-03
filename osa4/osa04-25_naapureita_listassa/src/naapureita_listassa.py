# tee ratkaisu tänne
def pisin_naapurijono(lista):
    arvot = []
    laskuri = 0
    varasto = 0

    # kaydaan lista lapi kayttaen valimuuttujaa
    for i in lista:
        # kaytetaan valimuuttujaa
        edellinen = varasto
        varasto = i

        # jos luku on sama kasvatetaan laskuria
        if (varasto - 1) == edellinen or (varasto + 1) == edellinen:
            laskuri = laskuri + 1
            arvot.append(laskuri)
        # muuten nollataan laskuri takaisin alkuun
        else:
            laskuri = 1
    
    return max(arvot)

if __name__ == "__main__":
    lista = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    toinen_lista = [1, 2, 5, 4, 3, 4]
    print(pisin_naapurijono(lista)) # 4
    print(pisin_naapurijono(toinen_lista)) # 4