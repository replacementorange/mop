# Kirjoita ratkaisu tähän
vuosi = int(input("Vuosi: "))
karkausvuosi = vuosi + 1

while True:
    if karkausvuosi % 4 == 0 and karkausvuosi % 100 != 0 or karkausvuosi % 400 == 0:
        break
    karkausvuosi += 1

print(f"Vuotta {vuosi} seuraava karkausvuosi on {karkausvuosi}")