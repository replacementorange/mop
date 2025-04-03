# tee ratkaisu tänne
# https://www.w3schools.com/python/ref_func_round.asp
# https://docs.python.org/3/library/decimal.html
def muotoile(lista):
    # uusi lista pyuoristetuille
    pyoristetys = []
    # kaydaan lista lapi
    for luku in lista:
        # pyoristetaan 2 desim. ja muutetaan str
        p_luku = f"{luku:.2f}"
        # lisataan p_luku listaan
        pyoristetys.append(p_luku)
    return pyoristetys

if __name__ == "__main__":
    lista = [1.234, 0.3333, 0.11111, 3.446]
    lista2 = muotoile(lista)
    print(lista2)