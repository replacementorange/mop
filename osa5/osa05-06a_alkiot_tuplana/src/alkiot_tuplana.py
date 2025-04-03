# tee ratkaisu tänne
def tuplaa_alkiot(luvut: list):
    uusi_lista = []
    for i in range(len(luvut)):
        uusi_lista.append(luvut[i] * 2)
    return uusi_lista

if __name__ == "__main__":
    luvut = [2, 4, 5, 3, 11, -4]
    tuplaluvut = tuplaa_alkiot(luvut)
    print("alkuperäinen:", luvut)
    print("tuplattu:", tuplaluvut)