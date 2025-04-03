# Kirjoita ratkaisu tähän
syote = input("Anna lause: ")
syote = " " + syote
kohta = 1

while kohta < len(syote):
    if syote[kohta - 1] == " " and syote[kohta] != " ":
        print(syote[kohta])
    kohta += 1