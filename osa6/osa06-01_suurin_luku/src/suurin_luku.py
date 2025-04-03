# tee ratkaisu tänne
def suurin():
    with open("luvut.txt") as tiedosto:
        rivit = tiedosto.readlines()
        luvut = [int(rivi.strip()) for rivi in rivit]
        return max(luvut)

if __name__ == "__main__":
    print(suurin())