"""
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
"""

class Cont:

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.")

    def debitare_cont(self, suma_cheltuita):
        if suma_cheltuita <= self.sold:
            self.sold -= suma_cheltuita
            print(f"Contul a fost debitat cu suma {suma_cheltuita} lei, iar soldul contului este {self.sold} lei")
        else:
            print("Fonduri insufuciente")

    def creditare_cont(self, suma_depusa):
        self.sold += suma_depusa

        print(f" A fost depusa suma de {suma_depusa} lei, iar soldul contului este {self.sold} lei")


cont_1 = Cont("RO001BNR", "Popescu Ion", 2500)
cont_2 = Cont("RO002BNR", "Cristescu Gigel", 10000)
cont_3 = Cont("RO003BNR", "Vasilescu Gigel", 1000)

cont_1.afisare_sold()
cont_1.debitare_cont(500)
cont_1.creditare_cont(300)
cont_2.afisare_sold()
cont_2.debitare_cont(5000)
cont_2.creditare_cont(250)
cont_3.afisare_sold()
cont_3.debitare_cont(1500)
cont_3.creditare_cont(1900)
