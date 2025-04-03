luku_yht = 0
luku_summa = 0
luku_ka = 0
luku_pos = 0
luku_neg = 0

print("Syötä kokonaislukuja, 0 lopettaa: ")
while True:
    luku = int(input("Luku: "))
    if luku == 0:
        print(f"Lukuja yhteensä {luku_yht}")
        print(f"Lukujen summa {luku_summa}")
        print(f"Lukujen keskiarvo {luku_ka}")
        print(f"Positiivisia {luku_pos}")
        print(f"Negatiivisia {luku_neg}")
        break
    else:
        if luku < 0:
            luku_neg += 1
        else:
            luku_pos += 1
        luku_yht += 1
        luku_summa += luku
        luku_ka = float(luku_summa / luku_yht)
