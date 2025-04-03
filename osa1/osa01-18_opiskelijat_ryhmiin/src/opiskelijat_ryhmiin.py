maara = int(input("Montako opiskelijaa? "))
koko = int(input("Mikä on ryhmän koko? "))
if (maara % koko == 0):
    print(f"Ryhmien määrä: {maara//koko}")
else:
    print(f"Ryhmien määrä: {(maara//koko) + 1}")