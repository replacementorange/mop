# tee ratkaisu tänne
def pituus(lista):
    return len(lista)

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    vastaus = pituus(lista)
    print("vastaus", vastaus)

    vastaus = pituus([1, 1, 1, 1])
    print("vastaus", vastaus)