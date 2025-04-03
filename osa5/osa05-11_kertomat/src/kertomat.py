# tee ratkaisu tänne
def kertomat(n: int):
    # tyhja sanakirja
    sanakirja = {}
    kertoma = 1
    # kaydaan lapi luvut
    for luku in range(1, n+1):
        # kerrotaan luku
        kertoma *= luku
        # sijoitetaan luku sanakirjaan
        sanakirja[luku] = kertoma
    return sanakirja

if __name__ == "__main__":
    k = kertomat(5)
    print(k[1])
    print(k[3])
    print(k[5])