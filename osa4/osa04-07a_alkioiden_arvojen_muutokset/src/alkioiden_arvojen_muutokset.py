# Kirjoita ratkaisu tähän
lista = [1, 2, 3, 4, 5]

while True:
    indeksi = int(input("Anna indeksi: "))
    if indeksi == -1:
        break
    numero = int(input("Anna arvo: "))
    lista[indeksi] = numero
    print(lista)