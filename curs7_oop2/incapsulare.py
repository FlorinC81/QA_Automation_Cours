"""
Pilonii OOP in engleza inheritance (mostenire), abstraction (abstractizare),
polymorphism (polimorfism) si encapsulation (incapsulare)

4. Incapsulare (Encapsulation) - posibilitatea de a PROTEJA atributele clasei, folosind modificatorii de vizibilitate
- private (privat, adica atributul poate fi accesat DOAR din interiorul clasei in care a fost definit )
   se defineste cu dublu underscore in fata (__asa)
- protected (protejat, adica atributul poate fi accesat din clasa in care a fost definit,
  dar si din clasele copii ale acesteia, INSA nu din exterior)
  se defineste cu un singur underscore (_asa)

  Atunci cand avem un atribut ascuns (privat), putem folosi niste metode speciale
  pentru a interactiona cu el numite getter (pt a-l vedea) si setter (pt a-i schimba valoarea)
 In general, metodele acestea  se vor denumi cu set_ /get_ PLUS numele initial al variabilei

 class x:
    __ceva

    def get_ceva(self):
        return __ceva

    def set_ceva(self, ceva_nou):
        __ceva = ceva_nou
"""

class Factura:
# Atributele de clasa, daca modificam o data, modificam pentru toate obiectele

    __seria = "XYZ" # atributele cu doua underscore in fata sunt PRIVATE
    numar = 1

    def __init__(self, nume_produs, cantitate, pret_buc):
        self.nr_fact = Factura.numar
        self.prod = nume_produs
        self.cantitate = cantitate
        self.pret = pret_buc
        Factura.numar += 1
    #gettr
    def get_seria(self):
        return self.__seria
    #setter
    def schimba_seria(self, noua_serie):
        self.__seria = noua_serie

    def descrie(self):
        print(f"{self.__seria} {self.nr_fact}")
        print(f"{self.prod} {self.cantitate} {self.pret} {self.cantitate* self.pret}")

f1 = Factura("Telefon", 10, 120)
print(f1.seria, f1.nr_fact)

f2 = Factura("TV", 5, 70)
f2.seria = "ABC"
print(f2.seria, f2.nr_fact)
print(f1.seria, f1.nr_fact)
