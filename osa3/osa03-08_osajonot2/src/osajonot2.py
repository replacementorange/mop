mjono = str(input("Anna merkkijono: "))
mjono = mjono[::-1]
alku = 0

while alku < len(mjono):
    print(mjono[alku::-1])
    alku += 1