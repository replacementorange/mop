print("Henkilö 1:")
eka_nimi = str(input("Nimi:  "))
eka_ika = int(input("Ikä: "))

print("Henkilö 2:")
toka_nimi = str(input("Nimi:  "))
toka_ika = int(input("Ikä: "))


if eka_ika > toka_ika:
    print(f"Vanhempi on {eka_nimi}")
elif eka_ika < toka_ika:
    print(f"Vanhempi on {toka_nimi}")
else:
    print(f"{eka_nimi} ja {toka_nimi} ovat yhtä vanhoja")