# tee ratkaisu tähän
def tulosta_monesti(mjono, x):
    i = 0
    while i < x:
        print(mjono)
        i += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    tulosta_monesti("python", 5)