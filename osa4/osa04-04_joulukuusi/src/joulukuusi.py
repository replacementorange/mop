# tee ratkaisu tänne
def joulukuusi(koko):
    print("joulukuusi!", end="")
    i = 0
    while i <= koko:
        print(" " * (koko - i) + "*" * (2 * i - 1))
        i += 1
        if i > koko:
            print(" " * (koko*2 - i) + "*")
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    joulukuusi(3)