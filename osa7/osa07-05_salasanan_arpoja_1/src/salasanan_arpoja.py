# tee ratkaisu tänne
# https://stackoverflow.com/questions/2030053/how-to-generate-random-strings-in-python
import random, string

def luo_salasana(pituus: int):
    kirjaimet = string.ascii_lowercase
    return ''.join(random.choice(kirjaimet) for i in range(pituus))

if __name__ == "__main__":
    for i in range(10):
        print(luo_salasana(8))