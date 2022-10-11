import math
from abc import ABC
"""
Pilonii OOP in engleza inheritance (mostenire), abstraction (abstractizare),
polymorphism (polimorfism) si encapsulation (incapsulare)

2. Abstractizarea: ca si mostenirea, DAR clasa parinte este o clasa abstracta,
adica nu putem face obiecte din ea si o folosim doar ca si un template
pentru metodele pe care ar trebui sa le implementeze copiii.

Clasa abstracta trebuie sa mosteneasca clasa ABC (from abc import ABC)
Fiecare metoda a clasei abstracte trebuie sa arunce exceptia NotImplementedError
Clasa abstracta nu are constructor deoarece nu putem face obiecte abstracte.

3. Polimorfism -> poli (mai mult), morfis (forma/forme)=> eva care poate lua mai multe forme
In cazul nostru, o functie care desi are acelasi nume are implementari sau definitii diferite
Exemple: functiile aria si perimetrul 
"""

class FormaGeometrica(ABC):

    def aria(self):
        raise NotImplementedError

    def perimetru(self):
        raise NotImplementedError


class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.r = raza

    def aria(self):
        return self.r**2 * 3.14

    def perimetru(self):
        return self.r* 3.14


class Dreptunghi(FormaGeometrica):

    def __init__(self, lat1, lat2):
        self.l1 = lat1
        self.l2 = lat2

    def aria(self):
        return self.l1 * self.l2

    def perimetru(self):
        return 2*(self.l1 + self.l2)

    def diagonala(self):
        return math.sqrt(self.l1**2+ self.l2**2)

cerc = Cerc(10)
drept = Dreptunghi(5,3)
print(cerc.aria())
print(drept.aria())

print(cerc.perimetru())
print(drept.perimetru())

print(drept.diagonala())

lista_fg = [Cerc(4), Dreptunghi(2,7), Cerc(10), Dreptunghi(5,5),Dreptunghi(9,7), Cerc(12)]
for fg in lista_fg:
    print()
    print(f"Perimetru: {fg.perimetru()}")
    print(f"Aria: {fg.aria()}")