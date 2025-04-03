# tee ratkaisu tänne
from string import ascii_letters, digits

def vaihda_koko(merkkijono: str):
    return merkkijono.swapcase()

def puolita(merkkijono: str):
    kp = len(merkkijono) // 2
    return (merkkijono[:kp]), merkkijono[kp:]

def poista_erikoismerkit(merkkijono: str):
    sallitut_merkit = ascii_letters + digits + "ÅåÄäÖö "
    uudet_merkit = ""
    for merkki in merkkijono:
        if merkki in sallitut_merkit:
            uudet_merkit += merkki
    return uudet_merkit

if __name__ == "__main__":
    import merkkiapuri
    mjono = "Moi kaikki!"

    print(merkkiapuri.vaihda_koko(mjono))

    p1, p2 = merkkiapuri.puolita(mjono)

    print(p1)
    print(p2)

    m2 = merkkiapuri.poista_erikoismerkit("Tämä on testi, katsotaan miten käy!!!11!")
    print(m2)