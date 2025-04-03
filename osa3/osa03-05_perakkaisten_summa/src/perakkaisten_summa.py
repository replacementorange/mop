asti = int(input("Mihin asti: "))
summa = 0
lisattava = 1
lausunto = ""

while summa < asti:
    if summa < asti:
        lausunto += f"{lisattava}"
        lausunto += " + "
    
    summa += lisattava
    lisattava += 1

print(f"Laskettiin {lausunto[:-2]}= {summa}")