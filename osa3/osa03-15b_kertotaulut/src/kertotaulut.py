luku = int(input("Anna luku: "))
i = 1

while i <= luku:
    j = 1
    while j <= luku:
        lasku = i * j
        print(f"{i} x {j} = {lasku}")
        j += 1
    i += 1