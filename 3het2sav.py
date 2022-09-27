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

"""print(kocsi_1.futott_km)
print(Kocsi.negy_kereke_van)
print(Kocsi.szamlalo)
print(kocsi_2.kiir_szin())
print()
kocsi_1.fut(1000)
print(kocsi_1.futott_km)
print(kocsi_2.futott_km)
print()"""

class RandomBag:

    def __init__(self):
        self.content = []

    def __str__(self):
        return "[RandomBag] : " + str(self.content)

    def __ad__(self, other):
        tmp = []

        for item in self.content:
            tmp.append(item)
        for item in other.content:
            tmp.append(item)
        return tmp

    def put(self, object):
        self.content.append(object)

    def pop(self):
        if len(self.content) > 0:
            index = np.random.randint(0, len(self.content))
            item = self.content[index]
            del self.content[index]
            return item
        else:
            return "Bag is empty"

    def size(self):
        return len(self.content)

bag = RandomBag()
bag.put("Alma")

print(bag.size())
print(bag)
print(bag.pop())
print(bag.pop())
print()

for i in range(1, 11):
    bag.put(i)

while bag.size() > 0:
    print(bag.pop())
