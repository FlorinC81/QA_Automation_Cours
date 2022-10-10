# Input este functia cu care preluam date de la utilizator(de la tastatura)
nume = input("Introdu numele: \n")

print(f"Salut {nume}!")

# by default, ce primim de la input este INTOTDEAUNA string

varsta = input("Cati ani ai? \n")

print(type(varsta))
# Daca dorim alte tipuri de date , va trebui sa facem type casting
varsta = int(varsta)
print(type(varsta))

# Exercitiu cu asert si input: Cod CAPCHA
rezultat_capcha = int(input("Cat este 12 + 21 \n"))
assert rezultat_capcha == 33, "Nu esti om, esti robot"