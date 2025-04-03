# tee ratkaisu tänne

# luetaan tekstitiedosto
with open("wordlist.txt") as tiedosto:

    # luodaan sanalista
    sanalista = []
    for rivi in tiedosto:
        rivi = rivi.replace("\n", "")
        sanalista.append(rivi)

# pyydetaan kayttajan syote
syote = input("Write text: ")

# muutetaan syote yksittaisiksi sanoiksi
sanat = syote.split(" ")
# poimitaan korjattavat
korjatut_sanat = []

# kaydaan syote lapi
for sana in sanat:
    # Jos virheellinen, poimitaan se
    if sana.lower() not in sanalista:
        korjatut_sanat.append(f"*{sana}*")
    else:
        korjatut_sanat.append(sana)

korjattu_syote = ""
for sana in korjatut_sanat:
     korjattu_syote = korjattu_syote + sana + " "

print(korjattu_syote)