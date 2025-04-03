# tee ratkaisu tänne
def lue(kayttajan_syote: str, alaraja: int, ylaraja: int):
    while True:
        try:
            syote = int(input(kayttajan_syote))
            if alaraja <= syote <= ylaraja:
                return syote
            else:
                print(f"Syötteen on oltava kokonaisluku väliltä {alaraja}...{ylaraja}")
        except ValueError:
            print(f"Syötteen on oltava kokonaisluku väliltä {alaraja}...{ylaraja}")

if __name__ == "__main__":
    luku = lue("syötä luku: ", 5, 10)
    print("syötit luvun:", luku)