"""
Exceptii: clase speciale Python folosite atunci cand ceva nu merge bine in cod
Folosind mecanismul try-except pentru a gestu=iona posibilele exceptii aparute in codul nostru,
astfel incat programul sa NU se opreasca

try:
    incercam ceva aici
    care s-ar putea sa dea exceptie
except NumeExceptie as e:
    aici gestionam exceptia cum consideram noi
"""

l = [1,2,3,4]
print(l[0])
# Daca as decomenta linia de mai jos codul s-ar opri cu eroare
#print(l[220])
try:
    print(l[5])
except IndexError as e:
    print("Am dat de o eroare de tipul IndexError")
    print(e)

print(l[3])

"""
Unde am putea folosi try-except:
-imput de la utilizator (verificam daca am primit ce asteptam noi)
"""
# try:
#     varsta = int(input("Introduceti varsta:"))
#     print(f"Ati introdus {varsta}")
# except ValueError as e:
#     print("Nu ati introdus un numar")
#
# print("La revedere")

"""
Reguli pentru prinderea exceptiilor:
- avem mereu un singur try, dar putem avea mai multe except
-daca avem mai multe exceptii posibile, trebuie sa le punem de la cea mai specifica, la cea mai generica 
- la final putem avea inclusiv un except "gol", 
  care sa cuprinda orice alta exceptie la care nu ne-am gandit noi 
"""
try:
    nr_par = int(input("Introduceti un numar par:"))
    assert nr_par % 2 == 0, "Oups..."
#except ValueError as e: => daca facem as e, ii dam practic un nume de variabila exceptiei si o putem folosi apoi in blocul ei
except ValueError as e:
    print("Nu ati introdus un numar")
except AssertionError as e:
    print("Numarul nu este par")
    print(e)
except:
    # In general nu vrem sa facem asta (adica sa nu specificam exceptia pe care o prindem )
    print("A aparut alta exceptie, nu stim care...")

print("Am terminat")