eka = str(input("Anna 1. kirjain: "))
toka = str(input("Anna 2. kirjain: "))
kolmas = str(input("Anna 3. kirjain: "))

if eka < toka < kolmas or kolmas < toka < eka:
    print(f"Keskimmäinen kirjain on {toka}")
elif toka < eka < kolmas or kolmas < eka < toka:
    print(f"Keskimmäinen kirjain on {eka}")
else:
    print(f"Keskimmäinen kirjain on {kolmas}")