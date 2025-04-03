ika = int(input("Kerro ikäsi? "))

if ika < 0:
    print("Taitaa olla virhe")
elif ika == 0 or ika < 5:
    print("En usko, että osaat kirjoittaa...")
else:
    print(f"Ok, olet siis {ika}-vuotias")
