# tee ratkaisu tänne
def kertaa_kymmenen(alku: int, loppu: int):
    # tyhja sanakirja
    sanakirja = {}
    # kaydaan lapi kaikki alun ja lopun valilla olevat
    for i in range(alku, loppu+1):
        # kerrotaan arvo
        sanakirja[i] = i * 10
    return sanakirja

if __name__ == "__main__":
    d = kertaa_kymmenen(3, 6)
    print(d)