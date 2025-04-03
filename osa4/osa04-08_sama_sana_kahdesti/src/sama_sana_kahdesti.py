# Kirjoita ratkaisu tähän
sanat = []

while True:
    sana = str(input("Anna sana: "))
    if sana in sanat:
        break
    sanat.append(sana)
print(f"Annoit {len(sanat)} eri sanaa")