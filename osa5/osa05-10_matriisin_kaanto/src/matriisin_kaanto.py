# tee ratkaisu tänne
# transponoi eli i --> j ja j --> i --> [i][j] = [j][i] ja toisinpain
# 2 x for
def transponoi(matriisi: list):
    # matriisin pituus
    pituus = len(matriisi)
    # kaydaan lapi matriisi 2 x for silmukalla
    for i in range(pituus):
        for j in range(i + 1, pituus): # esim i=1, j=2
            # kaannetaan arvot
            matriisi[i][j], matriisi[j][i] = matriisi[j][i], matriisi[i][j]

if __name__ == "__main__":
    matriisi = [1,2,3], [4,5,6], [7,8,9]
    print(matriisi)
    transponoi(matriisi)
    print(matriisi)