# tee ratkaisu tänne
def shakkilauta(x):
    for i in range(x):
        for j in range(i+1, i+1+x):
            print(j%2, end="")
        print()

# kokeillaan funktiota kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    shakkilauta(3)
    print
    shakkilauta(4)
