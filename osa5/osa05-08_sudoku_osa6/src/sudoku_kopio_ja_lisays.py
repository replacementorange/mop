# tee ratkaisu tänne
def tulosta(sudoku: list):
    i = 1
    # kaydaan lapi rivit
    for rivi in sudoku:
        # rivit vaaka
        for x in range(0, 9, 3):
            # rivit pysty
            for y in range(0, 3):
                if rivi[x+y] == 0:
                    print("_ ", end="")
                else:
                    print(rivi[x+y],"", end="")

            if (x != 6):
                print(" ", end="")
            else:
                print()
                
        if i in (3, 6):
            print()
        i += 1

def kopioi_ja_lisaa(sudoku: list, rivi_nro: int, sarake_nro: int, luku:int):
    # kopio listasta
    kopio = []
    # kaydaan rivit lapi ja lisataan ne
    for rivi in sudoku:
        kopio.append(rivi[:])
    kopio[rivi_nro][sarake_nro] = luku
    return kopio

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    kopio = kopioi_ja_lisaa(sudoku, 0, 0, 2)
    print("Alkuperäinen:")
    tulosta(sudoku)
    print()
    print("Kopio:")
    tulosta(kopio)