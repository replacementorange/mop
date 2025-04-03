# tee ratkaisu tänne
def lukukirja():
    # Sanakirja luvuille
    luvut = {}

    # ykkoset
    # Sanakirja ykkosille
    ykkoset = {0:"nolla", 1:"yksi", 2:"kaksi", 3:"kolme", 4:"neljä", 5:"viisi", 6:"kuusi", 7:"seitsemän", 8:"kahdeksan", 9:"yhdeksän"}
    # kymppi
    luvut[10] = "kymmenen"

    for i in range(10):
        luvut[i] = ykkoset[i]

    # toista
    for i in range(1, 10):
        luvut[i + 10] = ykkoset[i] + "toista"
    
    # -kymmenta
    for i in range(2, 10):
        luvut[i * 10] = ykkoset[i] + "kymmentä"
        for j in range(1, 10):
            luvut[i * 10 + j] = ykkoset[i] + "kymmentä" + ykkoset[j]

    return luvut

if __name__ == "__main__":
    luvut = lukukirja()
    print(luvut[2])
    print(luvut[11])
    print(luvut[45])
    print(luvut[99])
    print(luvut[0])