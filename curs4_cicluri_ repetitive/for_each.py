note_muzicale = ["do","re","mi","fa","sol","la","si","do"]
for idx in range(len(note_muzicale)):
    print(f"La indexul {idx} am gasit nota muzicala {note_muzicale[idx]}")
print()
# For each
#   facem ceva cu elementul respectiv
# Unde colectie  = lista, set, dictionar, tupla
for nota in note_muzicale:
    print(f"Nota muzicala este: {nota}")
print()

# Vreau sa aflu de cate ori apare nota do in lista , dara sa folosesc count
count_do = 0
for nota in note_muzicale:
    print(f"Acum testez {nota}...")
    if nota == "do":
        count_do += 1
        print(f"Am gasit un do, contorul a ajuns acum la {count_do}!")

print(f"Am gasit nota do in lista de note muzicale de {count_do} ori")

"""
Problema:  vreua sa gasesc notax (primita de la utilizator) in note muzicale 
daca o gasesc vreau sa ma opresc prima data cand o gasesc 
daca  nu exista in lista , vreau sa afisez ca nu exista.
"""

# break - for-ul  se opreste automat cand intalneste un break, chiat daca mai existau elemente in colectie
nota_cautata = input("Introduceti nota cautata:")
gasit = False # Flag pt a sti daca am gasit ce cautam sau nu

for nota in note_muzicale:
    print(f"Acum testam nota {nota}...")
    if nota == nota_cautata:
        print("Am gasit nota cautata de dvs!")
        gasit = True
        break
if not gasit:
    print(f"Nu am gasit nota cautata de dvs!")
print(f"Am terminat bucla de cautare!")


# varianta 2 pt problema de mai sus

for nota in note_muzicale:
    print(f"Acum testam nota {nota}...")
    if nota == nota_cautata:
        print("Am gasit nota cautata de dvs!")
        break
else:
    #Aici se junge doar daca for-ul a ajuns la final fara sa dea de vreun break
    print("Nu am gasit nota cautata!")

"""
For - else
Atunci cand folosim break intr-un for, putem avea si o ramura else pt for,
care va fi executata DOAR DACA for-ul a rulat fara a ajunge deloc la break
"""

# Vreau sa printez toate notele muzicale, mai putin cele care incep cu "s"
print("Notele muzicale care NU incep cu s sunt:")
for nota in note_muzicale:
     if nota[0] == "s":
        # sari peste aceasta nota, nu vreau sa o printez, deoarece incepe cu s
        continue
     print(nota)
#vreau sa afisez numerele mai mici ca 10 care nu sunt du=ivizibile cu 3
for index in range(10):
    if index % 3 == 0:
        continue
    print(f"Numarul {index} nu este divizibil cu 3!")