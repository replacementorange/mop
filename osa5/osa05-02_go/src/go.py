# tee ratkaisu tänne
def kumpi_voitti(pelilauta: list):
    # Pelaajien pisteet
    pelaaja1 = 0
    pelaaja2 = 0

    # Kaydaan rivi
    for rivi in pelilauta:
        # Kaydaan arvo
        for ruutu in rivi:
            if ruutu == 1: # Pelaaja 1 saa pisteen
                pelaaja1 += 1
            elif ruutu == 2: # Pelaaja 2 saa psiteen
                pelaaja2 += 1
    # Jos p1 enemman pisteita
    if pelaaja1 > pelaaja2:
        return 1
    # Jos p2 enemman pisteita
    elif pelaaja2 > pelaaja1:
        return 2
    # Jos tasapeli
    else:
        return 0

if __name__ == "__main__":
    pelilauta = [[1, 2, 2, 2], [2, 1, 1, 1], [0, 2, 1, 0]]
    print(kumpi_voitti(pelilauta))