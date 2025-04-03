pisteet = int(input("Anna pisteet [0-100]: "))

if pisteet > 100:
    print("Arvosana: mahdotonta!")
elif pisteet <= 100 and pisteet >= 90:
    print("Arvosana: 5")
elif pisteet <= 89 and pisteet >= 80:
    print("Arvosana: 4")
elif pisteet <= 79 and pisteet >= 70:
    print("Arvosana: 3")
elif pisteet <= 69 and pisteet >= 60:
    print("Arvosana: 2")
elif pisteet <= 59 and pisteet >= 50:
    print("Arvosana: 1")
elif pisteet <= 49 and pisteet >= 0:
    print("Arvosana: hylätty!")
else:
    print("Arvosana: mahdotonta!")
