"""
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul

self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
"""

class Dreptunghi:
    def __init__(self,lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f"Dreptunghiul are lungimea de {self.lungime}, latimea de {self.latime} si culoarea {self.culoare}")
        print()

    def aria(self):
        return self.latime * self.lungime

    def perimetru(self):
        return  self.latime*2 + self.lungime*2

    def schimba_culoare(self, culoare):
        self.culoare = culoare


dreptunghi_1 = Dreptunghi(5,3, "alb")
print(dreptunghi_1.perimetru())
print(dreptunghi_1.aria())
dreptunghi_1.descrie()
print(dreptunghi_1.culoare)

dreptunghi_1.schimba_culoare("rosu")
print(dreptunghi_1.culoare)
dreptunghi_1.descrie()
