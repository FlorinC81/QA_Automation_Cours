# Avem 3 operaori logici (funf=ctioneaza doar pe variabile boolean):and, or, not
# And - conditie de tip SI: x and y => atat x cat si y trebuie sa fie adevarat
are_permis = True
varsta = 21

# And - ambele conditii trebuie sa fie adevarate pt ca resultatul sa fie adevarat
assert are_permis and varsta > 18, "Nu ai voie sa conduci o masina"

nota1, nota2, nota3 = 7, 3, 8
assert nota1 > 4 and nota2 >4 and nota3 > 4, "Ai picat"

# OR -x sau y: adevarat daca cel putin una dintre conditiile x sau y este adevarata
assert nota1 > 4 or nota2 >4 or nota3 > 4, "Nu ai trecut la niciun examen"

#NOT - Operatorul de negare: Transforma True in False si viceversa

major = varsta > 18
assert not major, "Esti major"