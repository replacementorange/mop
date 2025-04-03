# tee ratkaisu tänne
def tallenna_henkilo(henkilo: tuple):
    # maaritellaa henkilo
    nimi, ika, pituus = henkilo
    # maaritellaan tiedosto
    kaytettava_tiedosto = "henkilot.csv"
    
    # avataan tiedosto (luo tiedoston jos ei ole olemassa)
    with open(kaytettava_tiedosto, 'a') as tiedosto:
        # rivi tiedostoon
        rivi = f"{nimi};{ika};{pituus}\n"
        # kirjoitetaan tiedostoon
        tiedosto.write(rivi)

if __name__ == "__main__":
    henkilo = ("Kimmo Kimmonen", 37, 175.5)
    tallenna_henkilo(henkilo)