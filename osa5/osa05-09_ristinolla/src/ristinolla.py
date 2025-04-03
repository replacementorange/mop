# tee ratkaisu tänne
def pelaa_siirto(lauta: list, x: int, y: int, nappula: str):
    # tarkistetaan, etta kukaan ei ole voittanut ja kohta on tyhja
    if 0 <= x < 3 and 0 <= y < 3 and lauta[y][x] == "":
        # asetetaan merkki nappulaan
        lauta[y][x] = nappula
        return True
    else:
        # kerrotaan siirron olevan mahdoton
        return False

if __name__ == "__main__":
    lauta = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(pelaa_siirto(lauta, 2, 0, "X"))
    print(lauta)