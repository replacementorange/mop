# tee ratkaisu tänne
def rivi_oikein(sudoku: list, rivi_nro: int):
    # rivi
    rivi = sudoku[rivi_nro]
    # Tarkistetut luvut
    tarkistetut = []
    for luku in rivi:
        if luku > 0 and luku in tarkistetut: # Jos luku suurempi kuin nolla ja on esiintynyt
            return False
        tarkistetut.append(luku) # Jos ei ole niin lisataan se
    return True

if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(rivi_oikein(sudoku, 0))
    print(rivi_oikein(sudoku, 1))