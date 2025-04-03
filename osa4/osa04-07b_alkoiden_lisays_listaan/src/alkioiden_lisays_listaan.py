# Kirjoita ratkaisu tähän
lista = []

maara = int(input("Kuinka monta lukua: "))

i = 1
while i <= maara:
    luku = int(input(f"Anna luku {i}: "))
    i += 1
    lista.append(luku)
print(lista)