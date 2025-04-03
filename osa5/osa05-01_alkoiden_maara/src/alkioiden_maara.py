# tee ratkaisu tänne
def laske_alkiot(matriisi: list, alkio: int):
    maara = 0
    # HUOM EI KAYDA NUMEROA VAAN KOKO RIVI LAPI
    for rivi in matriisi:
        # Nyt kaydaan numero
        for luku in rivi:
            if luku == alkio:
                maara += 1
    return maara



if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(laske_alkiot(m, 1)) # 3
    print(laske_alkiot(m, 2)) # 1