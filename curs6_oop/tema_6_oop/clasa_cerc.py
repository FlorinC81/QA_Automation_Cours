"""
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
"""

class Cerc:
    def __init__(self, raza, culoare = "verde"):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f"Cercul are raza de {self.raza} si culoarea {self.culoare}")

    def aria(self):
        pi = 3.14
        return self.raza ** 2 * pi

    def diametrul(self):
        return self.raza * 2

    def circumferinta(self):
        return self.raza *(2*3.14)

cerc_1 = Cerc(3)
cerc_1.raza
cerc_1.descrie_cerc()
print(cerc_1.aria())
print(cerc_1.diametrul())
print(cerc_1.circumferinta())

