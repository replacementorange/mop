# tee ratkaisu tänne
from datetime import datetime

d = int(input("Päivä: "))
m = int(input("Kuukausi: "))
a = int(input("Vuosi: "))

sv = datetime(a, m, d)
pvm = datetime(1999, 12, 31)

if sv > pvm:
    print("Et ollut syntynyt, kun vuosituhat vaihtui.")
else:
    paivat = pvm - sv
    print(f"Olit {paivat.days} päivää vanha, kun vuosituhat vaihtui.")