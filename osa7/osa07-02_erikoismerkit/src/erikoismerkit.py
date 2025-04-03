# tee ratkaisu tänne
import string

def jaa_merkkeihin(merkkijono: str):
    osa1 = ""
    osa2 = ""
    osa3 = ""

    for merkki in merkkijono:
        if merkki in string.ascii_letters:
            osa1 = osa1 + merkki
        elif merkki in string.punctuation:
            osa2 = osa2 + merkki
        else:
            osa3 = osa3 + merkki
    return osa1, osa2, osa3

if __name__ == "__main__":
    osat = jaa_merkkeihin("Tämä on testi!!! Toimiiko, mitä?")
    print(osat[0])
    print(osat[1])
    print(osat[2])