mjono = input("Sana: ")
max_pituus = 20
rivi = "*"

if len(mjono) < 20:
    max_pituus -= len(mjono)
    lisa = rivi * max_pituus
    print(lisa + mjono)
else:
    print(mjono)