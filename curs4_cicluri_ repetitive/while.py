# While  - este un ciclu repetitiv in care nu stim exact nr de pasi , dat stim ca avem o conditie de indeplinot
#WHILE - cat timp
# while conditie:
#   fa ceva

i = 0
while i < 5:
    print(i)
    i+=1 # daca nu incrementam noi i-ul, programul va crapa deoarece bucla se va repeta pana cand ramane fara memorie

"""
In realitate, vom folosi while aunci cand nu stim exact cat timp trebuie sa executam un cod,
dar avem o conditie de oprire. Exemple:
- validarea unui input de la utilizator
- validare user/parola
- pt a forta un nr maxim de incercari pt o anumita actiune
"""

age_is_correct = False
while not age_is_correct:
    age = int(input("Varsta dvs:"))
    if 1 < age <99:
        age_is_correct = True
    else:
        print("Varsta nu este corecta, trebuie sa fie intre 1 si 99. Incercati din nou")

user, parola = "adela", "helloworld"
print("Nu sunteti logat, trebie sava logati")
nr_incercari = 0
nr_max_incercari = 3

"""
while-else functioneaza la fel ca si for-else
pe ramura else se va ajunge doar daca while-ul se termina si nu a ajuns deloc la un break.
"""
while nr_incercari <nr_max_incercari:
     my_password = input("introduceti parola:")
     if parola == my_password:
        print("Felicitari, sunteti logat cu succes!")
        break
     else:
        print("Parola gresita, incercati din nou!")


     nr_incercari += 1
     print(f"Ai incercat sa te loghezi de {nr_incercari} ori!")
     print(f"Mai ai {nr_max_incercari - nr_incercari} incercari ramase...")
else:
    print("Ai incercat de 3 ori sa te loghezi, nu mai ai voie sa incerci timp de un minut")
print("Am terminat cu logarea!")

