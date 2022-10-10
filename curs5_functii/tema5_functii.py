#1.Funcție care să calculeze și să returneze suma a două numere

def suma(a, b):
    suma_2 = a+b
    return suma_2


a = int(input("Introduceti primul numar:\n"))
b =  int(input("Introduceti al 2 lea numar:\n"))

print(f"Suma celor 2 numere introduse este {suma(a,b)}")


# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

def functie(x):
    if x % 2 == 0:
        return True
    else:
        return False
x = int(input("introdu numarul:\n"))
print(functie(x))
#3. Funcție care returnează numărul total de caractere din numele tău complet.
#    (nume, prenume, nume_mijlociu)

def nume_return(a, b, c):
    lungime_nume = len(a + b + c)
    return lungime_nume

nume = str(input("Introdu numele:\n"))
prenumele1 = str(input("Introdu primul prenumele:\n"))
prenumele2 = str(input("Introdu cel de al doilea prenumele:\n"))

print(f"Lungimea numelui este {nume_return(nume, prenumele1, prenumele2)}")


#4. Funcție care returnează aria dreptunghiului

def a_d (a, b):
    aria_drept = (a * b)
    return aria_drept

a = int(input("Introdu lungimea:\n"))
b = int(input("Introdu latimea:\n"))

print(f"Aria dreptunfhiului este egala cu {a_d(a, b)}")

#5. Funcție care returnează aria cercului

def a_c(r):
    aria_cerc = 3.14*r**2
    return aria_cerc

raza = float(input("Introdu raza cercului: "))
print(f"Aria cercului este {a_c(raza)}")


# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
#  și Talse dacă nu găsește.

def gaseste(x, sir):
    for element in sir:
        if element == x:
            return True
    return False


print(gaseste("c", "crocodil"))


"""
7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
"""

def str(sir):
    litere_mici = 0
    litere_mari = 0
    for i in sir:
        if i.isupper():
            litere_mari += 1
        elif i.islower():
            litere_mici += 1
    print(f"Numarul de caractere mici {litere_mici} \nNumarul de caractere mari {litere_mari}")

str1 = input(f"Intoduceti un string cu litere masi si mici:\n")
str(str1)

# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu numerele pozitive


lista = [2, 3, 5, -5, -3, 6, -4, 8, 9, -1, 0]
def alege(sir):
    lista_pozitive = []
    for idx in sir:
        if idx> 0:
            lista_pozitive.append(idx)
    return lista_pozitive
print(alege(lista))

"""
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
"""

def compara(x,y):
    if x>y:
        print(f"Primul număr {x} este mai mare decat al doilea nr {y}")
    elif x<y:
        print(f"Al doilea nr {y} este mai mare decat primul nr {x}")
    else:
        print("Numerele sunt egale")

x = int( input("introdu primul numar:\n"))
y = int( input("introdu al doilea numar:\n"))

compara(x,y)

"""
10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
"""
def functie(numar, set_de_numere):
    if numar not in set_de_numere:
        set_de_numere.add(numar)
        print(f"{numar} a fost adaugat in set")
        return True
    else:
        print(f"{numar} nu a fost adaugat, deoarece exista.")
        return False
functie(5, {8,3,-5,23,-9,4,12,-85})