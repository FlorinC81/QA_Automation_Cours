
# variabila - este o zona de memorie care tine date

print("EX 2")
marca_masina ="Mazda"  #string
cilindree_masina = 1998  #integer
lungime_masina = 5.51   #float
inmatriculata = True  #boolean
print(f'')

print("EX 3")
print(type(marca_masina))
print(type(cilindree_masina))
print(type(lungime_masina))
print(type(inmatriculata))

print("EX 4")
lungime_masina = round(lungime_masina)
print(f"Noua lungime a masinii va fi: {lungime_masina} m")
print(f"Variabila 'lungime_masina' dupa rotunjire este de tipul {type(lungime_masina)}")

print("EX 5")
# int-> float
my_cilindree_masina = float(cilindree_masina)
print(my_cilindree_masina, type(my_cilindree_masina))
# bool-> str
my_inmatriculata = str(inmatriculata)
print(my_inmatriculata,type(my_inmatriculata))

print(f'Am o masina marca {marca_masina} si are motorul de {cilindree_masina} cmc')
print(f'Masina are lungimea de {lungime_masina} m')
print(f'Acest autoturism este inmatriculat in Romania? - {inmatriculata}')

print("EX 6")
nume = input("Introdu numele \n")
prenume = input("Introdu prenumele \n")


print(f"Numele complet are {len(nume+prenume)} caractere")

print("EX 7")

lungimea = float(input("Introdu lungimea \n"))
latimea = float(input("Introdu latimea \n"))

print(f"Aria dreptunghiului este {lungimea*latimea} ")

print("EX 8")

str1 = "Coral is either the stupidest animal or the smartest rock"
str2 = "the"
print(str1)
print(f"Cuvantul 'the' apare de {str1.count(str2)} ori in textul de mai sus.")


print("EX 10")

assert type(str1) == int, f"Nu contine numere"