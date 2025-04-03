# tee ratkaisu tänne
def risunelio(x):
    i = 0
    while i < x:
        print("#" * x)
        i += 1


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)