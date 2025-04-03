# tee ratkaisu tänne
def pisin(merkkijonot: list):
    pisin_mjono = ""
    for sana in merkkijonot:
        if len(sana) > len(pisin_mjono):
            pisin_mjono = sana


    return pisin_mjono

if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))