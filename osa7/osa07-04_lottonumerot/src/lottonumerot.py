# tee ratkaisu tänne
import random

def lottonumerot(maara: int, alaraja: int, ylaraja: int):
    numerot = random.sample(range(alaraja, ylaraja + 1), maara)
    return sorted(numerot)



if __name__ == "__main__":
    for numero in lottonumerot(7, 1, 40):
        print(numero)