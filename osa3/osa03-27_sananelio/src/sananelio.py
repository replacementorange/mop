# tee ratkaisu tänne
def nelio(merkit: str, koko: int):
    i = 0
    rivi = ""

    # nelio = kanta * korkeus
    while i < koko * koko:
        # tarkistetaa tasaisuus
        if i > 0 and i % koko == 0:
            print(rivi)
            rivi = ""
        # muuten tulostetaan
        rivi += merkit[i % len(merkit)]
        i = i + 1
    print(rivi)

if __name__ == "__main__":
    nelio("ab", 3)
    print()
    nelio("aybabtu", 5)