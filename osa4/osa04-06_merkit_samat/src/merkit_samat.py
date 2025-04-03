# tee ratkaisu tänne
def samat(str, index1, index2):
    if index1 >= len(str) or index2 >= len(str):
        return False
    return str[index1] == str[index2]

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":

    print(samat("koodari", 1, 2)) # True

    # eri merkit k ja a
    print(samat("koodari", 0, 4)) # False

    # toinen indeksi ei ole merkkijonon sisällä
    print(samat("koodari", 0, 10)) # False