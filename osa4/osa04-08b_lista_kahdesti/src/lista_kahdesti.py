# Kirjoita ratkaisu tähän
lista = []

while True:
    luku = int(input("Annan luku: "))
    if luku == 0:
        print("Moi!")
        break
    else:
        lista.append(luku)
        jarjestetty = sorted(lista)
    print(f"Lista: {lista}")
    print(f"Järjestettynä: {jarjestetty}")