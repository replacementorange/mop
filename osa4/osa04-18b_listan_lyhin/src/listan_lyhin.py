# tee ratkaisu tänne
def lyhin(lista):
    lyhin = lista[0]
    for alkio in lista:
        if len(alkio) <= len(lyhin):
            lyhin = alkio
    return lyhin

if __name__ == "__main__":
    lista = ["eka", "toka", "kolmas", "seitsemäs"]
    tulos = lyhin(lista)
    print(tulos) # eka

    lista = ["pekka", "emilia", "johanna", "venla", "eero", "antti"]
    tulos = lyhin(lista)
    print(tulos) # eero