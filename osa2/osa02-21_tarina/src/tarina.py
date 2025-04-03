sanat = ""
viimeinen_sana = ""

while True:
    sana = input("Anna sana: ")
    if sana == "loppu" or viimeinen_sana == sana:
        print(sanat)
        break
    else:
        sanat += sana + " "
        viimeinen_sana = sana

