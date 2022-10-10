
"""
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
"""
class Angajat:

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self. salariu = salariu

    def descrie(self):
        print(f"Angajatul {self.nume} {self.prenume} are salariul de {self.salariu}")

    def nume_complet(self):
        print(f"Numele complet al angajatului este {self.nume} {self.prenume}")

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        print(f"Salariul angajatului {self.nume} {self.prenume} va fi marit cu {procent} %")
        self.salariu += procent * self.salariu/100
        return self.salariu





angajat_1 = Angajat("Popescu", "Ion", 2500)
angajat_2 = Angajat("Ionescu", "Vasile", 4000)

angajat_1.descrie()
angajat_2.descrie()
angajat_1.nume_complet()
angajat_2.nume_complet()
print(angajat_1.salariu_lunar())
print(angajat_2.salariu_lunar())
print(angajat_1.salariu_anual())
print(angajat_2.salariu_anual())
print(angajat_1.marire_salariu(20))
print(angajat_2.marire_salariu(10))

