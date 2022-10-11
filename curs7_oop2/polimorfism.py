"""
Polimorfism: mai multe functii cu acelasi nume, dar comportament  sau parametri diferiti
Metoda language este polimorfica, deoarece returneaza lucruri diferite in functie de obiectul
care o apeleaza, DAR numele metodei este acelasi .
"""
class Romania:

    def language(self):
        return "ro"

class Franta:

    def language(self):
        return "fr"

inst_ro = Romania()
inst_fr = Franta()

print(inst_ro.language())
print(inst_fr.language())