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

