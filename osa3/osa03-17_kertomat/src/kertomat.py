while True:
    luku = int(input("Anna luku: "))
    if luku <= 0:
        print("Kiitos ja moi!")
        break

    else:
        i = 1
        j = luku
        while j >= 1:
            i = i * j
            j = j - 1
    print (f"Luvun {luku} kertoma on {i}")