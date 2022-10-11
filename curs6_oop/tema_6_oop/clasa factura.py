
"""
1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți

Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
"""
class Factura:
    def __init__(self, numar, nume_produs, cantitate, pret_bucata, serie ="AB"):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_bucata = pret_bucata
        self.serie = serie

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate
        return cantitate

    def schimba_pretul(self, pret_buc):
        self.pret_bucata = pret_buc
        return pret_buc


    def schimba_nume_produs(self, nume):
        self.nume_produs = nume
        return nume



factura_1 = Factura ( "001", "calorifer 10 elementi", 5, 450)
factura_2 = Factura ( "002", " Mithubishi AC 12000 BTU", 3, 3230)

print(factura_1.schimba_cantitatea(8))
print(factura_2.schimba_cantitatea(5))
print(factura_1.schimba_pretul(500))
print(factura_2.schimba_pretul(3485))
print(factura_1.schimba_nume_produs("Telefon"))
print(factura_2.schimba_nume_produs("Televizor"))

