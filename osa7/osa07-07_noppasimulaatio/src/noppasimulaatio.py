# tee ratkaisu tänne
from random import sample

def heita(noppa: str):
    nopat = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4]
    }

    heitto = sample(nopat[noppa], 1) [0]
    return heitto

def pelaa(noppa1: str, noppa2: str, kertaa: int):
    noppa1_voitto = 0
    noppa2_voitto = 0
    noppa_tasapeli = 0

    for i in range(kertaa):
        n1 = heita(noppa1)
        n2 = heita(noppa2)
        if n1 > n2:
            noppa1_voitto += 1
        elif n1 < n2:
            noppa2_voitto += 1
        else:
            noppa_tasapeli += 1
    return noppa1_voitto, noppa2_voitto, noppa_tasapeli

if __name__ == "__main__":
    for i in range(20):
        print(heita("A"), " ", end="")
    print()
    for i in range(20):
        print(heita("B"), " ", end="")
    print()
    for i in range(20):
        print(heita("C"), " ", end="")

    tulos = pelaa("A", "C", 1000)
    print(tulos)
    tulos = pelaa("B", "B", 1000)
    print(tulos)