# Exercitiul 1
'''
if-else = instructiunea if ( daca) executa un cod daca conditia este adevarata,
          si un alt cod (cu ajutorul lui else)  daca conditia nu este adevarata
'''

print("Exercitiul 2")
x = int(input("Introdu un numar:\n"))
if x >= 0:
    print("Numar natural")
else:
    print("Nu este numar natural")

print("Exercitiul 3")
if x < 0:
    print("Numar negativ")
elif x > 0:
    print("Numar pozitiv")
else:
    print("Numar neutru")

print("Exercitiul 4")
if (x > -2) and (x < 13):
    print("Numarul este intre -2 si 13")
else:
    print("Numarul nu este intre -2 si 13")

print("Exercitiul 5")
x = int(input("Introdu x:\n"))
y = int(input("Introdu y:\n"))
if (x-y) <5:
    print("Diferenta este mai mica decat 5")
else:
    print("Difenta este mai mare decat 5")

print("Exercitiul 6")

x = int(input("Introdu x:\n"))
if not (x < 5) and not(x > 27):
    print("Numarul este intre 5 si 27")
else:
    print("Numarul nu este intre 5 si 27")

print("Exercitiul 7")
x = int(input("Introdu x:\n"))
y = int(input("Introdu y:\n"))
if x == y:
    print("Valorile introduse sunt egale")
else:
    if x < y:
        print(f"{y} este mai mare")
    else:
        print(f"{x} este mai mare")

print("Exercitiul 8")

X = int(input("Latura 1:\n"))
y = int(input("Latura 2:\n"))
z = int(input("Latura 3:\n"))
if X == y and x == z and y == z:
    print("Triunghi echilateral")
elif X == y or x == z or y == z:
    print("Triunghi isoscel")
else:
    print("Triunghi oarecare")

print("Exercitiul 9")
litera = input("Introdu o litera:\n")
if litera in {"a", "e", "i", "o", "u"}:
    print("Litera este o vocala")
else:
    print("Litera introdusa nu este o vocala")

print("Exercitiul 10")
nota = float(input("Nota:\n"))
if nota > 9:
    print("A")
elif nota > 8:
    print("B")
elif nota > 7:
    print("C")
elif nota > 6:
    print("D")
elif nota > 4:
    print("E")
else:
    print("F")

# Exerctii optionale
# Ex 1
x = int(input("Introdu numarul:\n"))
if x > 999:
    print("Numarul introdus are minim 4 cifre")
else:
    print("Numarul introdus nu are minim 4 cifre")

# Ex 2
x = int(input("Introdu numarul:\n"))
if x > 99999 and x < 1000000:
    print("Numarul introdus are 6 cifre")
else:
    print("Numarul introdus nu are 6 cifre")

# Ex 3
x = int(input("Introdu numarul:\n"))
if x % 2 == 0:
     print("Numarul este par")
else:
    print("Numarul este impar")

#Ex 4

x = int(input("Introdu primul numar:\n"))
y = int(input("Introdu  al doilea numar:\n"))
z = int(input("Introdu al treilea numar:\n"))
if x > y and x > z:
    print("x este cel mai mare")
elif y > x and y > z:
    print("y este cel mai mare")
else:
    print("Z este cel mai mare ")

#Ex 5

print("Introdu valoarea unghiurilor pentru validare")
x = int(input("Introdu valoarea primului unghi:\n"))
y = int(input("Introdu valoarea celui de al doilea unghi:\n"))
z = int(input("Introdu valoarea celui de al treilea unghi:\n"))
if x+y+z == 180:
    print(" triunghi valid")
else:
    print("Triunghiul nu este valid")


# Ex 6
string = "Coral is either the stupidest animal or the smartest rock"
print(string)
x = int(input("Introdu numarul:\n"))
print(string[:len(string)-x])

# Ex 7

string2 = (string[0:5] + string[len(string)-5:len(string)])
print(string2)