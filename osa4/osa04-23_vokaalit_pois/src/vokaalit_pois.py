# tee ratkaisu tänne
def ilman_vokaaleja(mjono):
    uusi_mjono = ""
    for kirjain in mjono:
        if kirjain not in "aeiouyäöå":
            uusi_mjono += kirjain
    return uusi_mjono

if __name__ == "__main__":
    mjono = "tämä on esimerkki"
    print(ilman_vokaaleja(mjono)) # tm n smrkk