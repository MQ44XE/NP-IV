import numpy as np

class Kocsi():

    negy_kereke_van = True
    szamlalo = 0

    # __init__: konstruktor függvény, előkészít
    def __init__(self, szin, evjarat, futott_km, tipus):
        self.szin = szin
        self.evjarat = evjarat
        self.futott_km = futott_km
        Kocsi.szamlalo += 1
        self.tipus = tipus

    def kiir_szin(self):
        print(self.szin)

    def fut(self, ut):
        self.futott_km += ut

    def __str__(self):
        return "[Kocsi] szin: " + self.szin + "; evjarat: " + str(self.evjarat) + ";"

kocsi_1 = Kocsi("Fekete", 2020, 0, "Kamion")
kocsi_2 = Kocsi("Piros", 2017, 2500, "Sedan")

print(kocsi_1)


print(kocsi_1.futott_km)
print(Kocsi.negy_kereke_van)
print(Kocsi.szamlalo)
print(kocsi_2.kiir_szin())
print()
kocsi_1.fut(1000)
print(kocsi_1.futott_km)
print(kocsi_2.futott_km)