# Exercitiul 1

note_muzicale = ["do","re","mi","fa","sol","la","si","do"]
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)

note_muzicale.reverse()
print(note_muzicale)

# Exercitiul 2
print(note_muzicale.count('do'))

# Exercitiul 3
l1 = [3, 1, 0, 2]
l2 = [6, 5, 4]
l3 = l1+l2
print(l3)

l1.extend(l2)
print(l1)

# Exercitiul 4
l3.sort()
print(l3)
index_0 = l3.index(0)
print(f"Cifra 0 are indexul {index_0}")
l3.remove(0)
print(f"noua lista este {l3}")


# Exercitiul 5
if len(l3) != 0:
    print("Lista nu este goala")
else:
    print("Lista este goala")


# Exercitiul 6
l3.clear()
print(l3)

# Exercitiul 7
if len(l3) != 0:
    print("Lista nu este goala")
else:
    print("Lista este goala")

# Exercitiul 8

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

# Exercitiul 9

for i in dict1:
    print(f"{i} a luat nota {dict1[i]}")

# Exercitiul 10
dict1['Dorel'] = 6
print(f"Dupa contestatie Dorel a primit nota {dict1['Dorel']}")

# Exercitiul 11
del dict1['Gigel']
dict1['Ionica'] = 9
print(dict1)

# Exercitiul 12
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)

# Exercitiul 13
if weekend.issubset(zile_sapt):
    print("Weekend este un subset al zilelor din săptămânii.")
else:
    print("Weekend nu este un subset al zilelor din săptămânii.")

# Exercitiul 14
print(f"")
print(f"Diferentele dintre cele 2 seturi sunt:{zile_sapt-weekend}")

# Exercitiul 15
print(f"Elementele care se intersecteaza sunt: {zile_sapt.intersection(weekend)}")


# Optional

echipa = ["j1","j2","j3","j4","j5"]
