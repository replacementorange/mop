# tee ratkaisu tänne
def luvuista_suurin(int1, int2, int3):
    # https://docs.python.org/3/library/functions.html#max
    return max(int1, int2, int3)

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    suurin = luvuista_suurin(5, 4, 8)
    print(suurin)