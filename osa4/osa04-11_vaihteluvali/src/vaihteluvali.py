# tee ratkaisu tänne
def vaihteluvali(lista):
    vv = max(lista) - min(lista)
    return vv
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    vastaus = vaihteluvali(lista)
    print("vastaus", vastaus)