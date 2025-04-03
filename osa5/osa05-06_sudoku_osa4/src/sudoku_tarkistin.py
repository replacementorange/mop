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

def sarake_oikein(sudoku: list, sarake_nro: int):
    # Tarkistetut luvut
    tarkistetut = []
    # Tarkistetaan rivit
    for rivi in sudoku:
        luku = rivi[sarake_nro] # Hypitaan sarakkeiden rivien valilla
        if luku > 0 and luku in tarkistetut: # Jos luku suurempi kuin nolla ja on esiintynyt
            return False
        tarkistetut.append(luku) # Jos ei ole niin lisataan se
    return True

def nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int):
    # Nelio on 3 x 3
    # Tarkistetut luvut
    tarkistetut = []
    # rivit
    for rivi in range(rivi_nro, rivi_nro + 3): # +3 ,koska ruutu 3x3
        # sarakkeet
        for ruutu in range(sarake_nro, sarake_nro + 3): # sama homma kuin rivin kanssa
            luku = sudoku[rivi][ruutu] # luku ruudusta
            if luku > 0 and luku in tarkistetut: # Jos luku suurempi kuin nolla ja on esiintynyt
                return False
            tarkistetut.append(luku) # Jos ei ole niin lisataan se
    return True

# tarkista ruudukon rivit --> rivi_oikein
# tarkista ruudukon sarakkeet --> sarake_oikein
# tarkista ruukudon ruudut --> nelio_oikein
# jos menee lapi niin palauta --> true, muuten edellsiessa false
def sudoku_oikein(sudoku: list):
    for rivi in range(9): # kaydaan lapi rivit
        rivi = rivi_oikein(sudoku, rivi) # tarkistetaan meneeko rivi lapi
        if not rivi: # rivi ei mennyt lapi, eli koko ruudukko vaarin
            return False
    
    for sarake in range(9): # kaydaan lapi sarakkeet
        sarake = sarake_oikein(sudoku, sarake) # tarkistetaan meneeko lapi
        if not sarake: # jos ei mene lapi, koko ruudukko vaarin
            return False
        
    for rivi in range(0, 7, 3): # tarkistetaan kaikki 3x3 alueella olevat, aloitetaan rivilla
        for sarake in range(0, 7, 3): # sarakkeet
            nelio = nelio_oikein(sudoku, rivi, sarake) # nelio
            if not nelio: # jos vaarin
                return False
    return True




if __name__ == "__main__":
    sudoku1 = [
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
    print(sudoku_oikein(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]
    print(sudoku_oikein(sudoku2))