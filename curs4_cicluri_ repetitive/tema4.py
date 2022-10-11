# Exercitiul 1

mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for i in range(len(mașini)):
    print(f"Mașina mea preferată este {mașini[i]}.")
print()
for idx in mașini:
    print(f"Mașina mea preferată este {idx}")
print()

i = 0
while i < len(mașini):
    print(f"Mașina mea preferată este {mașini[i]}")
    i+=1
print()

#Exercitiul 2
for i in range(len(mașini)):
    if i == 0 or i == len(mașini)-1:
        continue
    mașini[i]= mașini[i].upper()
print(mașini)

print()

#Exercitiul 3

mașini = ['Audi', 'Volvo', 'BMW', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masina_cautata = 'Mercedes'
for i in mașini:
    if i == masina_cautata:
        print(i)
        print(f"Am găsit masina {masina_cautata} dorită de dvs")
        break
    else:
        print(f"Nu am gasit masina {masina_cautata}. Mai cautam")

print()

#Exercitiul 4

print("Va vom prezenta masinile pe care le consideram adecvate pentru dvs:")
for item in mașini:
    if item in ('Trabant', 'Lăstun'):
        continue
    print(f"S-ar putea sa va placa masina {item}")


#Exercitiul 5

masini_vechi = []
mașini = ['Audi', 'Volvo', 'BMW', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for idx in range(len(mașini)):
    if mașini[idx] == 'Lăstun' or mașini[idx] == 'Trabant':
        masini_vechi.append(mașini[idx])
        mașini[idx] = 'Tesla'
print(f"Lista masini actualizata este: {mașini} .")
print(f"lista masini vechi este: {masini_vechi} ")


print()


#Exercitiul 6

pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

buget = 15000
for masina, pret in pret_masini.items():
    if pret <= buget:
        print(f"Pentru bugetul de {buget} puteti cumpara urmatoarele modele {masina}")
print()

#Exercitiul 7

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
x = 0
for numar in  numere:
    if numar == 3:
        x = x+1
print(f"Numarul 3 apare de {x} ori in lista")


#Exercitiul 8

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0

for numar in numere:
    suma = suma + numar
print(f"Suma numerelor din lista este {suma}")

#Exercitiul 9

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
max = numere[0]
for numar in numere:
    if numar > max:
        max = numar
print(f"Cel mai mare numar din lista este {max}")


#Exercitiul 10
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
lista_neg = []
for numar in numere:
    if numar > 0:
        numar = numar - numar*2
    lista_neg.append(numar)
print(f"Lista a devenit: {lista_neg}")

