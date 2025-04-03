# tee ratkaisu tänne
import urllib.request
import json

def hae_kaikki():
    pyynto = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    kurssit = json.load(pyynto)
    aktiiviset = [(kurssi["fullName"],  kurssi["name"], kurssi["year"], sum(kurssi["exercises"])) for kurssi in kurssit if kurssi["enabled"]]
    return aktiiviset

def hae_kurssi(kurssi: str):
    pyynto = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{kurssi}/stats")
    viikot = json.loads(pyynto.read())
    opiskelijoita = 1
    tehtavia = 0
    tunteja = 0 
    
    for nro, viikko in viikot.items():
        if viikko['students'] > opiskelijoita:
            opiskelijoita = viikko['students']
        tunteja += viikko['hour_total']
        tehtavia += viikko['exercise_total']
    
    kurssi = {
        "viikkoja": len(viikot),
        "opiskelijoita": opiskelijoita,
        "tunteja": tunteja,
        "tunteja_keskimaarin": tunteja//opiskelijoita,
        "tehtavia": tehtavia,
        "tehtavia_keskimaarin": tehtavia//opiskelijoita,
    }

    return kurssi

if __name__ == "__main__":
    hae_kaikki()
    print(hae_kurssi("docker2019"))