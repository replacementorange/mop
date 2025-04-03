tuntipalkka = float(input("Tuntipalkka: "))
tyotunnit = int(input("Työtunnit: "))
viikonpaiva = str(input("Viikonpäivä: "))
palkka = (tuntipalkka * tyotunnit)

if (viikonpaiva == "sunnuntai"):
    print(f"Palkka {palkka*2} euroa")
else:
    print(f"Palkka {palkka} euroa")