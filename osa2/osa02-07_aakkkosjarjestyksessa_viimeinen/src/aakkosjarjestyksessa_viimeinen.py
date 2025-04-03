eka_sana = str(input("Anna 1. sana:"))
toka_sana = str(input("Anna 2. sana:"))

if eka_sana == toka_sana:
    print("Annoit saman sanan kahdesti.")
elif eka_sana < toka_sana:
    print(f"{toka_sana} on aakkosjärjestyksessä viimeinen.")
elif eka_sana > toka_sana:
    print(f"{eka_sana} on aakkosjärjestyksessä viimeinen.")