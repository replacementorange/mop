# tee ratkaisu tänne
from random import sample

def sanat(n: int, alku: str):
    lista = []
    sanat = ""

    # avataan tiedosto
    with open("sanat.txt") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            rivi = rivi.strip()
            if rivi.startswith(alku):
                lista.append(rivi)

    sanat = sample(lista, n)
    return sanat

if __name__ == '__main__':
    lista = sanat(3, "ca")
    for sana in lista:
        print(sana)